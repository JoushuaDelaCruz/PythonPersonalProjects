import time


class Stage:
    """
    A class responsible for running the game; It will print text on the command-line.
    This class has two main functions: start() and end().
    """

    def start(self):
        """
        Starts the game.
        """
        self._screen_writer("Welcome to the game!", 0.05)

    def end(self):
        """
        Ends the game.
        """
        pass

    @staticmethod
    def _screen_writer(text: str, delay: float):
        """
        Prints each character in text one by one on the command-line. 
        Higher delay means slower typing and vice versa.

        @param text: The text to be printed.
        @param delay: The delay between each character.
        """
        for character in text:
            print(character, end="", flush=True)
            time.sleep(delay)


def main():
    stage = Stage()
    stage.start()


if __name__ == "__main__":
    main()
