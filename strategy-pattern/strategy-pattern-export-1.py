#!/usr/bin/python

import json
from typing import Dict, List


def export_data(data: List[Dict[str, str]]):
    """
    Formats data, and saves to specified file.
    :param data: The data we want to export.
    """
    result_formatted = json.dumps(data, indent=4)
    print(result_formatted)


def main():
    data = [
        {"name": "Alice", "location": "Tokyo"},
        {"name": "Bob", "location": "Houston"},
    ]

    export_data(data)


if __name__ == "__main__":
    main()
