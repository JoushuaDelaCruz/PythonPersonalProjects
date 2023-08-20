from dotenv import load_dotenv
import os
import pytextrank
import spacy
import openai


class Summarizer:
    """
    A class responsible for summarizing given text. This class is dependent on spaCy and OpenAI.
    The engine the class uses is OpenAI's text-davinci-003 with max_tokens=100.
    """
    _nlp = None

    def __init__(self, text: str):
        """
        Initializes the summarizer with default engine, max_tokens and retrieves the api_key 
        from env file. It also sets up the spaCy nlp and nlp pipeline.

        param text: the text to summarize, a string
        """
        self._data = text
        self._engine = "text-davinci-003"
        self._max_tokens = 100
        self._setup_openai()
        self._setup_nlp()

    @property
    def text(self) -> str:
        """
        Returns the text to summarize.
        """
        return self._data

    @text.setter
    def text(self, text: str) -> None:
        """
        Sets the text to summarize.

        param text: the text to summarize, a string
        """
        self._data = text

    @staticmethod
    def _setup_openai():
        """
        Sets up the required information for OPENAI e.g. openai key
        """
        load_dotenv(dotenv_path=".\\.env")
        openai.api_key = os.getenv("OPENAI_KEY")

    def summarize(self) -> str:
        """
        Summarize the text given to the class using the OpenAI engine by getting the top 10 sentences
        """
        top_sentences = self._top_n_sentences(15)
        joined_sentences = self._join_sentences(top_sentences)
        summary = self._openai_request(joined_sentences)
        return summary

    @staticmethod
    def _join_sentences(sentences: list) -> str:
        """
        Joins each element in the sentences list to a single string.
        Created because each element is a type of spacy.tokens.span.Span, not a string,
        so str.join() cannot be used.
        """
        data = ""
        for span in sentences:
            sentence = span.text
            data += sentence + "\n"
        return data

    def _openai_request(self, sentences: str) -> str:
        """
        Makes a request to the OpenAI API to summarize the given sentences and returns the text.
        """
        response = openai.Completion.create(
            engine=self._engine,
            prompt=f"Using the top 10 rank sentences from a document. Summarize it: \n {sentences}",
            max_tokens=self._max_tokens,
        )
        return response.choices[0].text

    @classmethod
    def _setup_nlp(cls) -> None:
        """
        Sets up the spaCy nlp and nlp pipeline.
        """
        cls._nlp = spacy.load("en_core_web_lg")
        cls._nlp.add_pipe("textrank")

    def _top_n_sentences(self, n: int) -> list[str]:
        """
        Returns the top n sentences from a given text.

        param n: the total number of sentences to return, an integer, default 10
        return: the top n sentences, a list of strings
        """
        doc = self._nlp(self._data)
        top_sentences = [sentence for sentence in doc._.textrank.summary(
            limit_phrases=5, limit_sentences=n)]
        return top_sentences
