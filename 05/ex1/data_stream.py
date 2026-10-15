# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  data_stream.py                                    :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: laveerka                                  +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/09/24 13:37:45 by laveerka        #+#    #+#               #
#  Updated: 2026/10/15 15:05:45 by laveerka        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

from abc import ABC, abstractmethod
from typing import Any, Union, cast


class DataProcessor(ABC):
    def __init__(self) -> None:
        self.queue: list[str] = []
        self.rank: int = 0

    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    @abstractmethod
    def ingest(self, data: Any) -> None:
        pass

    def output(self) -> tuple[int, str]:
        item = self.queue.pop(0)
        rank = self.rank
        self.rank += 1
        return rank, item


class DataStream:
    def __init__(self) -> None:
        self._processors: list[DataProcessor] = []

    def register_processor(self, proc: DataProcessor) -> None:
        self._processors.append(proc)

    def process_stream(self, stream: list[Any]) -> None:
        for item in stream:
            for proc in self._processors:
                if proc.validate(item):
                    proc.ingest(item)
                    break
            else:
                print(f"DataStream error - Can't process element in stream: {item}")

    def print_processors_stats(self) -> None:
        print("== DataStream statistics ==")
        if not self._processors:
            print("No processor found, no data\n")
            return
        for proc in self._processors:
            name = type(proc).__name__.replace("Processor", " Processor")
            total = proc.rank + len(proc.queue)
            print(f"{name}: total {total} items processed, remaining {len(proc.queue)} on processor")


class NumericProcessor(DataProcessor):
    NumericData = Union[int, float, list[Union[int, float]]]

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

    def ingest(self, data: "NumericProcessor.NumericData") -> None:
        if not self.validate(data):
            raise ValueError("No valid numeric data")
        items = data if isinstance(data, list) else [data]
        self.queue.extend(str(item) for item in items)


class TextProcessor(DataProcessor):
    TextData = Union[str, list[str]]

    def validate(self, data: Any) -> bool:
        if isinstance(data, str):
            return True
        items: list[Any] = cast("list[Any]", data)
        return isinstance(data, list) and all(
            isinstance(item, str) for item in items
        )

    def ingest(self, data: "TextProcessor.TextData") -> None:
        if not self.validate(data):
            raise ValueError("No valid tet data")
        items = data if isinstance(data, list) else [data]
        self.queue.extend(items)


class LogProcessor(DataProcessor):
    LogData = Union[dict[str, str], list[dict[str, str]]]

    def validate(self, data: Any) -> bool:
        if isinstance(data, dict):
            items = cast("dict[Any, Any]", data)
            return all(
                isinstance(key, str) and isinstance(value, str)
                for key, value in items.items()
            )
        items: dict[Any, Any] = data
        return isinstance(data, list) and all(
            isinstance(item, dict) and self.validate(item) for item in items
        )

    def ingest(self, data: "LogProcessor.LogData") -> None:
        if not self.validate(data):
            raise ValueError("No valid log data")
        items = data if isinstance(data, list) else [data]
        self.queue.extend(": ".join(item.values()) for item in items)


def main() -> None:
    print("=== Code Nexus - Data Stream ===\n")
    print("Initialize Data Steam...")
    stream = DataStream()
    stream.print_processors_stats()
    print("Registering Numeric Processor\n")
    numeric = NumericProcessor()
    stream.register_processor(numeric)
    batch: list[Any] = ['Hello world', [3.14, -1, 2.71], [{'log_level':
                        'WARNING', 'log message':
                        'Telnet access! Use ssh instead'}, {'log_level': 'INFO', 'log_message':
                        'User wil is connected'}], 42, ['Hi', 'five']]
    print(f"Send first batch of data on stream: {batch}")
    stream.process_stream(batch)
    stream.print_processors_stats()
    print("\nRegistering other data processors")
    text = TextProcessor()
    log = LogProcessor()
    stream.register_processor(text)
    stream.register_processor(log)
    print("Send the same batch again")
    stream.process_stream(batch)
    stream.print_processors_stats()
    print("\nConsume some elements from the data processors: Numeric 3, Text 2, Log 1")
    for _ in range(3):
        numeric.output()
    for _ in range(2):
        text.output()
    for _ in range(1):
        log.output
    stream.print_processors_stats()


if __name__ == "__main__":
    main()
