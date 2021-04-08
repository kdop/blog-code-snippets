#!/usr/bin/python

import json
from typing import List, Dict
from abc import ABC, abstractmethod


class OutputHandlerInterface(ABC):
    @abstractmethod
    def handle(self, data: str):
        pass


class OutputToFile(OutputHandlerInterface):
    def __init__(self, filepath: str, mode: str = "w"):
        """
        OutputToFile constructor.
        :param filepath: Absolute path of file where data will be saved.
        :param mode: Mode in which the file is opened
        """
        self.filepath = filepath
        self.mode = mode

    def handle(self, data: str):
        with open(self.filepath, self.mode) as f:
            f.write(data)


def output_data(data: List[Dict[str, str]],
                output_handler: OutputHandlerInterface):
    """
    Formats and saves result to specified file.
    :param data: The data.
    :param output_handler: Handler object that outputs data as desired.
    :return: 
    """

    result_formatted = json.dumps(data, indent=4)
    output_handler.handle(result_formatted)


def main():
    data = [
        {"name": "Alice", "location": "Tokyo"},
        {"name": "Bob", "location": "Houston"}
    ]

    output_data(data, OutputToFile("output.json"))


if __name__ == "__main__":
    main()
