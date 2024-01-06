#!/usr/bin/python

import json
from abc import ABC, abstractmethod
from typing import Dict, List


class FormatHandler(ABC):
    @abstractmethod
    def format(self, data: List[Dict[str, str]]) -> str:
        """
        :param data: Data to format.
        :return: Formatted data.
        """
        pass


class FormatToJSON(FormatHandler):
    def __init__(self, indent: int = 4):
        """
        :param indent: Number of indentation spaces.
        """
        self.indent = indent

    def format(self, data):
        return json.dumps(data, indent=self.indent)


class FormatToCSV(FormatHandler):
    def __init__(self, separator: str = ","):
        """
        :param separator: Column separator string.
        """
        self.separator = separator

    def format(self, data):
        return "\n".join(
            [self.separator.join(list(row.values())) for row in data]
        )


class OutputHandler(ABC):
    @abstractmethod
    def handle(self, data: str):
        """
        :param data: Data to output.
        :return: None
        """
        pass


class OutputToConsole(OutputHandler):
    def handle(self, data):
        print(data)


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


def export_data(
    data: List[Dict[str, str]],
    format_handler: FormatHandler,
    output_handler: OutputHandler,
):
    """
    Formats data, and outputs according to specified OutputHandler.
    :param data: The data we want to export.
    :param format_handler: Handler object that formats data as desired.
    :param output_handler: Handler object that outputs data as desired.
    :return: None
    """
    output_handler.handle(format_handler.format(data))


class FormatHandlerFactory(object):
    inventory = {
        "json": FormatToJSON,
        "csv": FormatToCSV,
    }

    @staticmethod
    def build(item: str) -> FormatHandler:
        return FormatHandlerFactory.inventory[item]()


def main(format_name: str):
    data = [
        {"name": "Alice", "location": "Tokyo"},
        {"name": "Bob", "location": "Houston"},
    ]

    try:
        format_handler = FormatHandlerFactory.build(format_name)
    except KeyError:
        format_handler = FormatToJSON()  # default

    export_data(data, format_handler, OutputToConsole())


if __name__ == "__main__":
    format_name_clean = "csv"  # e.g. read this from argv
    main(format_name_clean)
