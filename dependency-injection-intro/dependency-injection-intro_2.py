#!/usr/bin/python

import json
from abc import ABC, abstractmethod
from typing import Dict, List


class OutputHandler(ABC):
    @abstractmethod
    def handle(self, data: str):
        """
        :param data: Data to output.
        :return: None
        """
        pass


class OutputToFile(OutputHandler):
    def __init__(self, filepath: str, mode: str = "w"):
        """
        :param filepath: Absolute path of file where data will be saved.
        :param mode: Mode in which the file is opened.
        """
        self.filepath = filepath
        self.mode = mode

    def handle(self, data):
        with open(self.filepath, self.mode) as f:
            f.write(data)


def export_data(data: List[Dict[str, str]], output_handler: OutputHandler):
    """
    Formats data, and outputs according to specified OutputHandler.
    :param data: The data we want to export.
    :param output_handler: Handler object that outputs data as desired.
    :return: None
    """
    result_formatted = json.dumps(data, indent=4)
    output_handler.handle(result_formatted)


def main():
    data = [
        {"name": "Alice", "location": "Tokyo"},
        {"name": "Bob", "location": "Houston"},
    ]

    export_data(data, OutputToFile("output.json"))


if __name__ == "__main__":
    main()
