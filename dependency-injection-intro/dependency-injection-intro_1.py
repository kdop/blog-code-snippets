#!/usr/bin/python

import json
from typing import List, Dict


def output_data(data: List[Dict[str, str]], filepath: str, mode: str = "w"):
    """
    Formats and saves result to specified file.
    :param data: The data.
    :param filepath: Absolute path of file where data will be saved.
    :param mode: Mode in which the file is opened
    :return: 
    """

    result_formatted = json.dumps(data, indent=4)

    with open(filepath, mode) as f:
        f.write(result_formatted)


def main():
    data = [
        {"name": "Alice", "location": "Tokyo"},
        {"name": "Bob", "location": "Houston"}
    ]

    output_data(data, "output.json")


if __name__ == "__main__":
    main()
