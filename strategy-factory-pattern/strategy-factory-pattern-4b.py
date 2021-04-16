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


def main():
    data = [
        {"name": "Alice", "location": "Tokyo"},
        {"name": "Bob", "location": "Houston"},
    ]

    export_data(data, JSONFormatHandler(), OutputToFile("output.json"))
    export_data(data, CSVFormatHandler(), OutputToConsole())


if __name__ == "__main__":
    main()
