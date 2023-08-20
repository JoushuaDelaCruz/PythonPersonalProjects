from pdf_reader import PDFReader
from text_filter import ExcessiveNewlinesFilter
from summarizer import Summarizer


def main():
    reader = PDFReader()
    content = reader.read("psychological_sample.pdf")
    summarizer = Summarizer(content)
    summary = summarizer.summarize()
    print(summary.strip())


if __name__ == "__main__":
    main()
