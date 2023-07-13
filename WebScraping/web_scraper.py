import requests
from bs4 import BeautifulSoup


class web_scraper:
    """
    This class functions as the web scraper of a specified website.
    """
    def scrape(url: str) -> BeautifulSoup:
        """
        Scrapes the specified website and a BeautifulSoup object containing all the html code.

        :param url: the website to be scraped, a string
        """
        response = requests.get(url)
        content = response.content
        return BeautifulSoup(content, "html.parser")
