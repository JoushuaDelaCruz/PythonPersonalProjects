from file_reader import PDFReader, TextReader, TextFileReader
from text_filter import ExcessiveNewlinesFilter
from summarizer import Summarizer
from request import setup_request_commandline


def _create_reader(file: str) -> TextReader:
    if file.endswith("pdf"):
        return PDFReader()
    return TextFileReader()


def summarize(file: str):
    """
    Summarize the given file from the request, and prints it to the user.
    If an error occur during the process, an error message will be printed instead.

    :param file: the file to be summarized
    """
    reader = _create_reader(file)
    content = reader.read(file)
    content = ExcessiveNewlinesFilter().strain(content)
    summarizer = Summarizer(content)
    summary = summarizer.summarize()
    print(summary.strip())


def main():
    request = setup_request_commandline()
    try:
        summarize(request.document)
    except Exception as e:
        print(e)
    finally:
        quit()


if __name__ == "__main__":
    main()
