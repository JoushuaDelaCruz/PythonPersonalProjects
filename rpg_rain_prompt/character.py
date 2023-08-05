import abc
from rpg_rain_prompt.attributes import AttributesFactory


class Character(abc.ABC):
    """
    Abstract class for creating of characters. Each subclass must implement
    the make_character function
    """
    @abc.abstractmethod
    def make_character(self, attributes: AttributesFactory):
        """
        Abstract method for creating of characters, using the CharacterAttributes as
        the data source.
        """
        pass
