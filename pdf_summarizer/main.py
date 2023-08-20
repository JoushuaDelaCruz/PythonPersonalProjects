from summarizer import Summarizer
from text_filter import ExcessiveNewlinesFilter


def main():
    data = ""
    with open("dilemma_sample.txt", "r", encoding="utf8") as text:
        for line in text:
            data += line
    data = ExcessiveNewlinesFilter.strain(data)
    summarizer = Summarizer(data)
    print(summarizer.summarize())


if __name__ == "__main__":
    main()
