class FormatHandlerFactory(object):
    inventory = {
        "json": JSONFormatHandler,
        "csv": CSVFormatHandler,
    }

    @staticmethod
    def build(item: str) -> FormatHandler:
        return FormatHandlerFactory.inventory[item]()
