import abc
import re


class TextFilter(abc.ABC):
    """
    An interface to filter text.
    """
    @staticmethod
    @abc.abstractmethod
    def strain(text) -> str:
        """
        Strain the text.

        :param text: The text to be strained.
        :return: The strained text.
        """
        pass


class ExcessiveNewlinesFilter(TextFilter):
    """
    A filter to remove excessive newlines except "\n" using regex.
    """
    @staticmethod
    def strain(text) -> str:
        """
        Strains the text of excessive newlines like "\n\n\n" replace it with "\n".

        :param text: The text to be strained.
        :return: The strained text.
        """
        cleaned_text = re.sub(r'(?<!\\)\\n|[\r\n]+', ' ', text)
        return cleaned_text
