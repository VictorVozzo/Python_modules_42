# ************************************************************************** #
#                                                                            #
#                                                        :::      ::::::::   #
#   data_stream.py                                     :+:      :+:    :+:   #
#                                                    +:+ +:+         +:+     #
#   By: vivozzo- <vivozzo-@student.42porto.com>    +#+  +:+       +#+        #
#                                                +#+#+#+#+#+   +#+           #
#   Created: 2026/06/18 15:51:37 by vivozzo-          #+#    #+#             #
#   Updated: 2026/06/18 15:51:38 by vivozzo-         ###   ########.fr       #
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


class DataStream:
    def __init__(self) -> None:
        self.processors: list[DataProcessor] = []

    def register_processor(self, proc: DataProcessor) -> None:
        if proc in self.processors:
            print("Processor was registered already!")
        else:
            self.processors.append(proc)

    def process_stream(self, stream: list[typing.Any]) -> None:
        if len(self.processors) == 0:
            print("No processor found!")
            return
        for item in stream:
            flag = 0
            for processor in self.processors:
                if processor.validate(item):
                    processor.ingest(item)
                    flag = 1
                    break
            if flag == 0:
                print(
                    "DataStream error - Can't process element in stream: "
                    f"{item}")

    def print_processors_stats(self) -> None:
        print("== DataStream statistics ==")
        if len(self.processors) == 0:
            print("No processor found, no data")
        else:
            for processor in self.processors:
                print(f"{processor.__class__.__name__}: total "
                      f"{processor.counter} items processed, remaining "
                      f"{len(processor.storage)} on processor")


def main() -> None:
    print("=== Code Nexus - Data Stream ===")
    print("\nInitialize Data Stream...")
    data_stream = DataStream()
    data_stream.print_processors_stats()
    print("\nRegistering Numeric Processor\n")
    numeric_processor = NumericProcessor()
    data_stream.register_processor(numeric_processor)
    data = ['Hello world', [3.14, -1, 2.71],
            [{'log_level': 'WARNING',
              'log_message': 'Telnet access! Use ssh instead'},
            {'log_level': 'INFO', 'log_message': 'User wil isconnected'}],
            42, ['Hi', 'five']]
    print(f"Send first batch of data on stream: {data}")
    data_stream.process_stream(data)
    data_stream.print_processors_stats()

    print("\nRegistering other data processors")
    text_processor = TextProcessor()
    log_processor = LogProcessor()
    data_stream.register_processor(text_processor)
    data_stream.register_processor(log_processor)
    print("Send the same batch again")
    data_stream.process_stream(data)
    data_stream.print_processors_stats()

    print("\nConsume some elements from the data processors: "
          "Numeric 3, Text 2, Log 1")
    for i in range(3):
        numeric_processor.output()
    for i in range(2):
        text_processor.output()
    log_processor.output()
    data_stream.print_processors_stats()


if __name__ == "__main__":
    main()
