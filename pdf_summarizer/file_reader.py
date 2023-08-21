import abc
from typing import TextIO

import PyPDF2
from PyPDF2 import PdfReader


class TextReader(abc.ABC):
    """
    A class responsible for reading text from a file only has one function
    that must be implemented: read()
    """

    def __init__(self):
        """
        Initialises the file and content private variables
        """
        self._file: str = ""

    @abc.abstractmethod
    def read(self, file_path: str) -> str:
        """
        Reads the content of a given file.

        @param file_path: the name of the file or path to the file.
        @return: the content of the file
        """
        pass

    @abc.abstractmethod
    def _check_file_type(self):
        """
        Checks the file's type

        @raises TypeError: if the file type is incorrect
        """
        pass


class PDFReader(TextReader):
    """
    A class responsible for reading pdf file
    """

    def read(self, file_path: str) -> str:
        """
        Reads the content of a pdf file.

        @param file_path: the file to read from
        @raises TypeError: if the file is not a pdf
        @raises FileNotFound: if the file cannot be found
        """
        self._file = file_path
        self._check_file_type()
        content = self._read_pdf()
        return content

    def _check_file_type(self):
        """
        Checks if the given file is a pdf file.

        @raises TypeError: if the file type is not pdf
        """
        if not self._file.endswith(".pdf"):
            raise TypeError("File must be a pdf file!")

    def _read_pdf(self) -> str:
        """
        Uses pyPDF2 to read the all text of the file. The file's text will all be
        stored in the content variable

        @raises FileNotFound: if file cannot be found
        """
        with open(self._file, 'rb') as pdf:
            reader = PdfReader(pdf, strict=False)
            return self._read_pages(reader)

    @staticmethod
    def _read_pages(reader: PdfReader):
        """
        Reads text from each pages of a pdfFileReader

        @param reader: A PdfFileReader to read each pages from
        """
        content = ""
        for page in reader.pages:
            content += page.extract_text()
        return content


class TextFileReader(TextReader):
    """
    A class responsible for reading a text file.
    """

    def read(self, file_path: str) -> str:
        """
        Reads the content of a text file.

        @param file_path: the file to read from
        @raises TypeError: if the file is not a pdf
        @raises FileNotFound: if the file cannot be found
        """
        self._file = file_path
        self._check_file_type()
        content = self._read_txt()
        return content

    def _check_file_type(self):
        """
        Checks if the given file is a text file.

        @raises TypeError: if file is not a text file
        """
        if not self._file.endswith(".txt"):
            raise TypeError("File must be a text file!")

    def _read_txt(self) -> str:
        """
        Reads the content of the text.

        @raise FileNotFound: if the file cannot be found.
        """
        with open(self._file, encoding="utf8") as txt:
            return self._read_pages(txt)

    @staticmethod
    def _read_pages(file: TextIO) -> str:
        """
        Reads each pages of a given file.

        @param file: the file to read the pages from, TextIO
        """
        content = ""
        for line in file:
            content += line
        return content
