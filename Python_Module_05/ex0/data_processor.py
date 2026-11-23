# ************************************************************************** #
#                                                                            #
#                                                        :::      ::::::::   #
#   data_processor.py                                  :+:      :+:    :+:   #
#                                                    +:+ +:+         +:+     #
#   By: vivozzo- <vivozzo-@student.42porto.com>    +#+  +:+       +#+        #
#                                                +#+#+#+#+#+   +#+           #
#   Created: 2026/06/17 10:58:31 by vivozzo-          #+#    #+#             #
#   Updated: 2026/06/17 10:58:32 by vivozzo-         ###   ########.fr       #
#                                                                            #
# ************************************************************************** #

import abc
import typing


class DataProcessor(abc.ABC):
    def __init__(self) -> None:
        self.storage: list[tuple[int, str]] = []
        self.counter = 0

    @abc.abstractmethod
    def validate(self, data: typing.Any) -> bool:
        pass

    @abc.abstractmethod
    def ingest(self, data: typing.Any) -> None:
        pass

    def output(self) -> tuple[int, str]:
        return self.storage.pop(0)


class NumericProcessor(DataProcessor):
    def validate(self, data: typing.Any) -> bool:
        is_number = isinstance(data, (int, float))
        is_list_number = (isinstance(data, list) and all(
            isinstance(item, (int, float)) for item in data))
        if is_number or is_list_number:
            return True
        else:
            return False

    def ingest(self, data: int | float | list[int | float]
               | list[int] | list[float]) -> None:
        if self.validate(data):
            if (isinstance(data, (int, float))):
                data_str = str(data)
                self.storage.append((self.counter, data_str))
                self.counter += 1
            else:
                for item in data:
                    data_str = str(item)
                    self.storage.append((self.counter, data_str))
                    self.counter += 1
        else:
            raise ValueError("Improper numeric data")


class TextProcessor(DataProcessor):
    def validate(self, data: typing.Any) -> bool:
        is_str = isinstance(data, str)
        is_list_str = (isinstance(data, list) and all(
            isinstance(item, str) for item in data))
        if is_str or is_list_str:
            return True
        else:
            return False

    def ingest(self, data: str | list[str]) -> None:
        if self.validate(data):
            if (isinstance(data, str)):
                self.storage.append((self.counter, data))
                self.counter += 1
            else:
                for item in data:
                    self.storage.append((self.counter, item))
                    self.counter += 1
        else:
            raise ValueError("Improper text data")


class LogProcessor(DataProcessor):
    def validate(self, data: typing.Any) -> bool:
        is_dict = isinstance(data, dict) and all(
            isinstance(k, str) for k in data.keys()) and all(
            isinstance(v, str) for v in data.values())
        is_list_dict = isinstance(data, list) and all(
            isinstance(item, dict)
            and all(isinstance(k, str) for k in item.keys())
            and all(isinstance(v, str) for v in item.values())
            for item in data)
        if is_dict or is_list_dict:
            return True
        else:
            return False

    def ingest(self, data: dict[str, str] | list[dict[str, str]]) -> None:
        if not self.validate(data):
            raise ValueError("Improper log data")

        if isinstance(data, dict):
            if len(data) == 2:
                data_str = str(data)
                self.storage.append((self.counter, data_str))
                self.counter += 1
        else:
            for item in data:
                if len(item) == 2:
                    self.storage.append(
                        (
                            self.counter,
                            f"{item['log_level']}: {item['log_message']}"
                        )
                    )
                    self.counter += 1


def main() -> None:
    print("=== Code Nexus - Data Processor ===\n")
    print("Testing Numeric Processor...")
    numeric = NumericProcessor()
    input_test_1 = 42
    print(
        f" Trying to validate input '{input_test_1}': "
        f"{numeric.validate(input_test_1)}")
    input_test_2 = "Hello"
    print(
        f" Trying to validate input '{input_test_2}': "
        f"{numeric.validate(input_test_2)}")
    input_test_2 = "foo"
    print(
        " Test invalid ingestion of string "
        f"'{input_test_2}' without prior validation:")
    try:
        numeric.ingest(input_test_2)  # type: ignore
    except Exception as e:
        print(f" Got exception: {e}")
    data_1 = [1, 2, 3, 4, 5]
    print(f" Processing data: {data_1}")
    numeric.ingest(data_1)
    print(" Extracting 3 values...")
    for i in range(3):
        rank, value = numeric.output()
        print(f" Numeric value {rank}: {value}")

    print("\nTesting Text Processor...")
    text = TextProcessor()
    input_test_1 = 42
    print(
        f" Trying to validate input '{input_test_1}': "
        f"{text.validate(input_test_1)}")
    data_2 = ["Hello", "Nexus", "World"]
    print(f" Processing data: {data_2}")
    text.ingest(data_2)
    print(" Extracting 1 value...")
    rank, value = text.output()
    print(f" Text value {rank}: {value}")

    print("\nTesting Log Processor...")
    log = LogProcessor()
    input_test_2 = "Hello"
    print(
        f" Trying to validate input '{input_test_2}': "
        f"{log.validate(input_test_2)}")
    data_3 = [{'log_level': 'NOTICE', 'log_message': 'Connection to server'},
              {'log_level': 'ERROR', 'log_message': 'Unauthorized access!!'}]
    print(f" Processing data: {data_3}")
    log.ingest(data_3)
    print(" Extracting 2 values...")
    for i in range(2):
        rank, value = log.output()
        print(f" Log entry {rank}: {value}")


if __name__ == "__main__":
    main()
