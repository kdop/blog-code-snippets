from abc import ABC, abstractmethod


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
