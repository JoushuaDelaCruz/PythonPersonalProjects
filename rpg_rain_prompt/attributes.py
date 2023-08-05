import abc


class AttributesFactory(abc.ABC):
    """
    A class responsible for attributes creation of characters. Each subclass must implement
    the make_attributes function.
    """

    def make_attributes(self):
        """
        Abstract method for creating of attributes
        """
        pass
