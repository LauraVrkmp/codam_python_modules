# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  data_processor.py                                 :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: laveerka                                  +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/09/24 13:37:37 by laveerka        #+#    #+#               #
#  Updated: 2026/10/02 14:51:02 by laveerka        ###   ########.fr        #
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


def main() -> None:
    print("=== Code Nexus - Data Processor ===\n")
    print("Testing Numeric Processor...")


if __name__ == "__main__":
    main()
