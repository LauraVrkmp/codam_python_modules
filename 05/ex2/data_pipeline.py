# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  data_pipeline.py                                  :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: laveerka <laveerka@student.codam.nl>      +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/09/24 13:37:50 by laveerka        #+#    #+#               #
#  Updated: 2026/10/20 23:32:00 by laveerka        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

from abc import ABC, abstractmethod
from typing import Any, Union, Protocol, cast


class DataProcessor(ABC):
    """Initialize a queue including rank"""
    def __init__(self) -> None:
        self.queue: list[str] = []
        self.rank: int = 0

    """Pass the validation"""
    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    """Pass the ingestion"""
    @abstractmethod
    def ingest(self, data: Any) -> None:
        pass

    """Return the rank and value of an item"""
    def output(self) -> tuple[int, str] | None:
        try:
            item = self.queue.pop(0)
        except IndexError:
            return None
        rank = self.rank
        self.rank += 1
        return rank, item


class ExportPlugin(Protocol):
    """General definition of the ExportPlugin to handle output"""
    def process_output(self, data: list[tuple[int, str]]) -> None:
        ...


class DataStream:
    """Initialize the list of DataProcessors as processors"""
    def __init__(self) -> None:
        self.processors: list[DataProcessor] = []

    """Append the DataProcessor to the processors"""
    def register_processor(self, proc: DataProcessor) -> None:
        self.processors.append(proc)

    """Process an item to the appropriate type"""
    def process_stream(self, stream: list[Any]) -> None:
        for item in stream:
            for proc in self.processors:
                if proc.validate(item):
                    proc.ingest(item)
                    break
            else:
                print(f"DataStream error - Can't process "
                      f"element in stream: {item}")

    """Print statistics of processed data"""
    def print_processors_stats(self) -> None:
        print("\n== DataStream statistics ==")
        if not self.processors:
            print("No processor found, no data\n")
            return
        for proc in self.processors:
            name = type(proc).__name__.replace("Processor", " Processor")
            total = proc.rank + len(proc.queue)
            print(f"{name}: total {total} items processed, remaining "
                  f"{len(proc.queue)} on processor")

    """Obtain a plugin item and forward to the appropriate plugin"""
    def output_pipeline(self, nb: int, plugin: ExportPlugin) -> None:
        for processor in self.processors:
            data: list[tuple[int, str]] = []
            for _ in range(nb):
                result = processor.output()
                if result is None:
                    break
                data.append(result)
            plugin.process_output(data)


class CSV_plugin:
    """Prints data in CSV format"""
    def process_output(self, data: list[tuple[int, str]]) -> None:
        values = [str(value) for _, value in data]
        print("CSV Output:")
        print(",".join(values))


class JSON_plugin:
    """Prints data in JSON format"""
    def process_output(self, data: list[tuple[int, str]]) -> None:
        json_str = ", ".join(f'"item_{iter}": "{value}"' for
                             iter, value in data)
        print("JSON Output:")
        print("{" + json_str + "}")


class NumericProcessor(DataProcessor):
    NumericData = Union[int, float, list[Union[int, float]]]

    """Return a bool whether the data is an int or float, or list of such"""
    def validate(self, data: Any) -> bool:
        if isinstance(data, (int, float)) and not isinstance(data, bool):
            return True
        items: list[Any] = cast("list[Any]", data)
        return (
            isinstance(data, list)
            and all(
                isinstance(item, (int, float)) and not isinstance(item, bool)
                for item in items
            )
        )

    """Ingest data of the NumericData type"""
    def ingest(self, data: "NumericProcessor.NumericData") -> None:
        if not self.validate(data):
            raise ValueError("No valid numeric data")
        items = data if isinstance(data, list) else [data]
        self.queue.extend(str(item) for item in items)


class TextProcessor(DataProcessor):
    TextData = Union[str, list[str]]

    """Return a bool whether the data is a string or list of such"""
    def validate(self, data: Any) -> bool:
        if isinstance(data, str):
            return True
        items: list[Any] = cast("list[Any]", data)
        return isinstance(data, list) and all(
            isinstance(item, str) for item in items
        )

    """Ingest data of the TextData type"""
    def ingest(self, data: "TextProcessor.TextData") -> None:
        if not self.validate(data):
            raise ValueError("No valid tet data")
        items = data if isinstance(data, list) else [data]
        self.queue.extend(items)


class LogProcessor(DataProcessor):
    LogData = Union[dict[str, str], list[dict[str, str]]]

    """Return a bool wether the data is a dictionary or list of such"""
    def validate(self, data: Any) -> bool:
        if isinstance(data, dict):
            items = cast("dict[Any, Any]", data)
            return all(
                isinstance(key, str) and isinstance(value, str)
                for key, value in items.items()
            )
        items_else: dict[Any, Any] = data
        return isinstance(data, list) and all(
            isinstance(item, dict) and self.validate(item)
            for item in items_else
        )

    """Ingest data of the LogData type"""
    def ingest(self, data: "LogProcessor.LogData") -> None:
        if not self.validate(data):
            raise ValueError("No valid log data")
        items = data if isinstance(data, list) else [data]
        self.queue.extend(": ".join(item.values()) for item in items)


def main() -> None:
    """Main to process datastreams, print statistics and process to CSV/JSON"""
    print("=== Code Nexus - Data Stream ===\n")
    print("Initialize Data Steam...")
    stream = DataStream()
    stream.print_processors_stats()
    print("Registering Processors\n")
    batch1: list[Any] = ['Hello world', [3.14, -1, 2.71],
                         [{'log_level': 'WARNING', 'log_message':
                           'Telnet access! Use ssh instead'},
                          {'log_level': 'INFO', 'log_message':
                          'User wil is connected'}],
                         42, ['Hi', 'five']]
    numeric = NumericProcessor()
    text = TextProcessor()
    log = LogProcessor()
    stream = DataStream()
    stream.register_processor(numeric)
    stream.register_processor(text)
    stream.register_processor(log)
    print(f"Send first batch of data on stream: {batch1}")
    stream.process_stream(batch1)
    stream.print_processors_stats()
    print("\nSend 3 processed data from each processor to a CSV plugin:")
    stream.output_pipeline(3, CSV_plugin())
    stream.print_processors_stats()
    batch2: list[Any] = [21, ['I love AI', 'LLMs are wonderful',
                              'Stay healthy'],
                             [{'log_level': 'ERROR', 'log_message':
                               '500 server crash'}, {'log_level':
                                                     'NOTICE', 'log_message':
                                                     'Certificate expires '
                                                     'in 10 days'}],
                             [32, 42, 64, 84, 128, 168], 'World hello']
    stream.process_stream(batch2)
    print(f"\nSend another batch of data {batch2}: ")
    stream.print_processors_stats()
    print("\nSend 5 processed data from each processor to a JSON plugin:")
    stream.output_pipeline(5, JSON_plugin())
    stream.print_processors_stats()


if __name__ == "__main__":
    main()
