# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  data_processor.py                                 :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: laveerka                                  +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/09/24 13:37:37 by laveerka        #+#    #+#               #
#  Updated: 2026/10/06 11:47:42 by laveerka        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

from abc import ABC, abstractmethod
from typing import Any, Union, cast


class DataProcessor(ABC):
    def __init__(self) -> None:
        self._queue: list[str] = []
        self._rank: int = 0

    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    @abstractmethod
    def ingest(self, data: Any) -> None:
        pass

    def output(self) -> tuple[int, str]:
        item = self._queue.pop(0)
        rank = self._rank
        self._rank += 1
        return rank, item


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
        self._queue.extend(str(item) for item in items)


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
        self._queue.extend(items)


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
        self._queue.extend(": ".join(item.values()) for item in items)


def numeric_processor() -> None:
    print("Testing Numeric Processor...")
    num_test: list[Any] = [42, "Hello"]
    numeric = NumericProcessor()
    for num in num_test:
        print(f"Trying to validate input '{num}': {numeric.validate(num)}")
    num_invalid: str = "foo"
    print(f"Test invalid ingestion of string '{num_invalid}'"
          f" without prior validation:")
    try:
        numeric.ingest(num_invalid)
    except ValueError:
        print("Got exception: Improper numeric data")
    num_valid: list[Any] = [1, 2, 3, 4, 5]
    print(f"Processing data: {num_valid}")
    numeric.ingest(num_valid)
    print("Extracting 3 values...")
    for _ in range(3):
        rank, value = numeric.output()
        print(f"Numeric value: {rank}: {value}")


def text_processor() -> None:
    print("\nTesting Text Processor...")
    text_invalid = 42
    text_proc = TextProcessor()
    print(f"Trying to validate input '{text_invalid}': "
          f"{text_proc.validate(text_invalid)}")
    text_data = ['Hello', 'Nexus', 'World']
    print(f"Processing Data: {text_data}")
    text_proc.ingest(text_data)
    print("Extracting 1 value...")
    rank, value = text_proc.output()
    print(f"Text value {rank}: {value}")


def log_processor() -> None:
    print("\nTesting Log Processor...")
    log_invalid = "Hello"
    log_proc = LogProcessor()
    print(f"Trying to validate input '{log_invalid}': "
          f"{log_proc.validate(log_invalid)}")
    log_data = [{'log_level': 'NOTICE', 'log_message': 'Connection to server'},
                {'log_level': 'ERROR', 'log_message': 'Unauthorized access!!'}]
    print(f"Processing data: {log_data}")
    log_proc.ingest(log_data)
    print("Extracting 2 values...")
    for _ in range(2):
        rank, value = log_proc.output()
        print(f"Log entry {rank}: {value}")


def main() -> None:
    print("=== Code Nexus - Data Processor ===\n")
    numeric_processor()
    text_processor()
    log_processor()


if __name__ == "__main__":
    main()
