from argparse import ArgumentParser
from dataclasses import dataclass, field


@dataclass
class Request:
    """
    Request represents a request to summarize a text file document.
    """
    _doc: str = field(default=None, init=False)

    def is_doc_empty(self):
        """
        Returns true if no input data in provided, else false
        """
        return self._doc is None

    @property
    def document(self):
        """
        Returns the file path.

        :return: the file path, a string
        """
        return self._doc

    @document.setter
    def document(self, new_doc):
        """
        Sets a new doc on the request.

        :param new_doc: the new file to process, a string
        """
        self._doc = new_doc


def _setup_parser() -> ArgumentParser:
    """
    A helper that sets up the ArgumentParser for the commandline.

    :return: an ArgumentParser
    """
    parser = ArgumentParser()
    parser.add_argument("file",
                        help="The file to summarize the text from. File can be pdf or txt file.")
    return parser


def _setup_request(parser: ArgumentParser) -> Request:
    """
    A helper that sets up the Request by using the input
    from the commandline parser.

    :return: a Request with the inputs
    """
    args = parser.parse_args()
    request = Request()
    request.document = args.inputfile
    return request


def setup_request_commandline() -> Request:
    """
    Implements the argparse module to accept arguments via commandline.
    This function specifies what these arguments are and parses it into
    an object of type Request. If error occurs with the provided
    arguments then function shows a message and exits the application.

    :return: a Request with the file given from the commandline
    """
    parser = _setup_parser()
    try:
        request = _setup_request(parser)
        return request
    except Exception as e:
        print(f"Error! Could not read arguments. \n {e}")
        quit()
