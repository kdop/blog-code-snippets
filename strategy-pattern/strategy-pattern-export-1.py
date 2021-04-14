#!/usr/bin/python

import json
from typing import Dict, List


def export_data(data: List[Dict[str, str]], filepath: str, mode: str = "w"):
    """
    Formats data, and saves to specified file.
    :param data: The data we want to export.
    :param filepath: Absolute path of file where data will be saved.
    :param mode: Mode in which the file is opened.
    :return: None
    """
    result_formatted = json.dumps(data, indent=4)
    with open(filepath, mode) as f:
        f.write(result_formatted)


def main():
    data = [
        {"name": "Alice", "location": "Tokyo"},
        {"name": "Bob", "location": "Houston"},
    ]

    export_data(data, "output.json")


if __name__ == "__main__":
    main()
