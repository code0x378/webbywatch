import logging
import sys
import random

import requests
from bs4 import BeautifulSoup
import time
import smtplib

from settings import *

logger = logging.getLogger("webby")


def check_url(url, keywords):
    response = requests.get(url, headers=HEADERS)
    soup = BeautifulSoup(response.text, "lxml")
    time.sleep(random.randint(DELAY_BETWEEN_URLS_MIN, DELAY_BETWEEN_URLS_MAX))
    return str(soup).find(keywords) < 0


def no_changes_found(url):
    logger.info(f"Checked {url} and found no changes")


def main():
    formatter = logging.Formatter(fmt='%(asctime)s:%(levelname)s: %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
    handler = logging.FileHandler('webbywatch.log', mode='w')
    handler.setFormatter(formatter)
    screen_handler = logging.StreamHandler(stream=sys.stdout)
    screen_handler.setFormatter(formatter)
    logger.setLevel(logging.DEBUG)
    logger.addHandler(handler)
    logger.addHandler(screen_handler)

    while True:
        for (url, keywords) in URLS.items():
            changed = check_url(url, keywords)
            if changed:
                still_changed = check_url(url, keywords)
                if still_changed:
                    logger.warning(f"Checked {url} and FOUND CHANGES!")
                    email_msg = f'Subject: WebbyWatch, {url} changed!\n\nThe following url was updated: {url}'
                    email_from = EMAIL_FROM
                    email_to = [EMAIL_TO]
                    server = smtplib.SMTP(EMAIL_HOST, EMAIL_PORT)
                    server.starttls()
                    server.login(EMAIL_HOST_USER, EMAIL_HOST_PASSWORD)
                    server.sendmail(email_from, email_to, email_msg)
                    server.quit()
                else:
                    no_changes_found(url)
            else:
                no_changes_found(url)

        time.sleep(DELAY_BETWEEN_CHECKS)


if __name__ == "__main__":
    main()