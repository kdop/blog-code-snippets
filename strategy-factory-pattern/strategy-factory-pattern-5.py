class FormatHandlerFactory(object):
    inventory = {
        "json": FormatToJSON,
        "csv": FormatToCSV,
    }

    @staticmethod
    def build(item: str) -> FormatHandler:
        return FormatHandlerFactory.inventory[item]()
