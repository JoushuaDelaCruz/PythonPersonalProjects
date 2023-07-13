from datetime import datetime
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os
import smtplib
from web_scraper import web_scraper
from dotenv import load_dotenv


class Robot:
    """
    A robot that runs the automated web scraping.
    """

    def __init__(self, from_email: str, to_email: str, password: str):
        """
        Initialises an automated robot that would send an email to the specified email address after running.

        :param from_email: the email address of the sender, a string
        :param to_email: the email address of the receiver, a string
        :param password: the password of the sender's email address, a string
        """
        self.server = 'smtp.gmail.com'
        self.port = 587
        self._to_email = to_email
        self._from_email = from_email
        self._password = password

    def compose_message(self, content: str):
        """
        Composes an email with the given content and send it to the email address specified in the .env file.

        :param content: the content of the email, a string
        """
        now = datetime.now()
        message = MIMEMultipart()
        message["From"] = self._from_email
        message["To"] = self._to_email
        message["Subject"] = f"Top CBC News [Automated Email] {now.day}/{now.month}/{now.year}"
        message.attach(MIMEText(content, 'html'))
        return message

    def send_email(self, message: MIMEMultipart):
        """
        Sends the message to the specified email address on the Robot private variables.

        :param message: the message to be sent, a MIMEMultipart object
        """
        with smtplib.SMTP(self.server, self.port) as connection:
            connection.set_debuglevel(1)
            connection.ehlo()
            connection.starttls()
            connection.login(self._from_email, self._password)
            connection.sendmail(
                self._from_email, self._to_email, message.as_string())
            connection.quit()

    @staticmethod
    def scrape(url: str):
        """
        Scrapes the specified url and returns the content.

        :param url: the url to be scraped, a string
        """
        content = f"<b> Canadian CBC News Top Stories: </b> <br> {'-' * 50} <br>"
        soup = web_scraper.scrape(url)
        for i, tag in enumerate(soup.find_all("h3", attrs={"class": "headline"}), start=1):
            content += f"{i} :: {tag.text} \n <br>"
        content += "<br> <br> <b> This email was sent by a robot. End of Message </b>"
        return content

    def run(self, url: str):
        """
        Runs the robot. Scraping the specified url and sending the email.
        """
        print("Running the robot...")
        content = self.scrape(url)
        message = self.compose_message(content)
        self.send_email(message)
        print("Robot has finished running.")


def main():
    load_dotenv(dotenv_path=".\.env")
    from_email = os.getenv("FROM_EMAIL")
    to_email = os.getenv("TO_EMAIL")
    password = os.getenv("PASSWORD")
    robot = Robot(from_email, to_email, password)
    url = "https://www.cbc.ca/news/canada"
    robot.run(url)


if __name__ == '__main__':
    main()
