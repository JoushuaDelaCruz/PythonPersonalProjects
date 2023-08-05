import abc


class Board(abc.ABC):
    """
    Abstract class for creating of boards. Each subclass must implement
    the make_board function
    """

    @abc.abstractmethod
    def make_board(self):
        """
        Abstract method for creating of boards
        """
        pass
