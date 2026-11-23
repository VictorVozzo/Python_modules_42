# ************************************************************************** #
#                                                                            #
#                                                        :::      ::::::::   #
#   data_pipeline.py                                   :+:      :+:    :+:   #
#                                                    +:+ +:+         +:+     #
#   By: vivozzo- <vivozzo-@student.42porto.com>    +#+  +:+       +#+        #
#                                                +#+#+#+#+#+   +#+           #
#   Created: 2026/06/19 12:15:19 by vivozzo-          #+#    #+#             #
#   Updated: 2026/06/19 12:15:20 by vivozzo-         ###   ########.fr       #
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


class ExportPlugin(typing.Protocol):
    def process_output(self, data: list[tuple[int, str]]) -> None:
        pass


class CSVPlugin:
    def process_output(self, data: list[tuple[int, str]]) -> None:
        list_len = len(data)
        print("CSV Output: ")
        if list_len == 1:
            print(f"{data[0][1]}", end="")
        else:
            print(f"{data[0][1]}", end="")
            for i in range(1, list_len):
                print(f",{data[i][1]}", end="")


class JSONPlugin:
    def process_output(self, data: list[tuple[int, str]]) -> None:
        list_len = len(data)
        print("JSON Output: ")
        if list_len == 1:
            print(f'{{"item_{data[0][0]}": "{data[0][1]}"}}', end="")
        else:
            print("{", end="")
            print(f'"item_{data[0][0]}": "{data[0][1]}"', end="")
            for i in range(1, list_len):
                print(f', "item_{data[i][0]}": "{data[i][1]}"', end="")
            print("}", end="")


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

    def output_pipeline(self, nb: int, plugin: ExportPlugin) -> None:
        for processor in self.processors:
            print()
            output_list: list[tuple[int, str]] = []

            if (nb > len(processor.storage)):
                nb = len(processor.storage)
            for i in range(nb):
                output_list.append(processor.output())
            plugin.process_output(output_list)


def main() -> None:
    print("=== Code Nexus - Data Pipeline ===\n")
    print("Initialize Data Stream...\n")
    data_stream = DataStream()
    data_stream.print_processors_stats()

    print("\nRegistering Processors\n")
    numeric_processor = NumericProcessor()
    data_stream.register_processor(numeric_processor)
    text_processor = TextProcessor()
    data_stream.register_processor(text_processor)
    log_processor = LogProcessor()
    data_stream.register_processor(log_processor)
    data = ['Hello world', [3.14, -1, 2.71],
            [{'log_level': 'WARNING',
              'log_message': 'Telnet access! Use ssh instead'},
            {'log_level': 'INFO', 'log_message': 'User wil isconnected'}],
            42, ['Hi', 'five']]
    print(f"Send first batch of data on stream: {data}\n")
    data_stream.process_stream(data)
    data_stream.print_processors_stats()

    nb = 3
    print(
        f"\nSend {nb} processed data from each processor to a CSV plugin:",
        end="")
    data_stream.output_pipeline(nb, CSVPlugin())
    print("\n")
    data_stream.print_processors_stats()

    data_2 = [21, ['I love AI', 'LLMs are wonderful', 'Stay healthy'],
              [{'log_level': 'ERROR', 'log_message': '500 server crash'},
              {'log_level': 'NOTICE',
               'log_message': 'Certificate expires in 10 days'}],
              [32, 42, 64, 84, 128, 168], 'World hello']
    print(f"\nSend another batch of data: {data_2}\n")
    data_stream.process_stream(data_2)
    data_stream.print_processors_stats()

    nb = 5
    print(
        f"\nSend {nb} processed data from each processor to a JSON plugin:",
        end="")
    data_stream.output_pipeline(nb, JSONPlugin())
    print("\n")
    data_stream.print_processors_stats()


if __name__ == "__main__":
    main()
