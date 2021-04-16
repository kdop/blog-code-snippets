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


class JSONFormatHandler(FormatHandler):
    def __init__(self, indent: int = 4):
        """
        :param indent: Number of indentation spaces.
        """
        self.indent = indent

    def format(self, data):
        return json.dumps(data, indent=self.indent)


class CSVFormatHandler(FormatHandler):
    def __init__(self, separator: str = ","):
        """
        :param separator: Column separator string.
        """
        self.separator = separator

    def format(self, data):
        return "\n".join(
            [self.separator.join(list(row.values())) for row in data]
        )
