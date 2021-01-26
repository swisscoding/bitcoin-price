#!/usr/local/bin/python3
# Made by @swisscoding on Instagram

from colored import stylize, fg
import requests
from bs4 import BeautifulSoup
import re

# decoration
print(stylize("\n---- | Get current Bitcoin price | ----\n", fg("red")))

# class
class Scraper:
    def __init__(self):
        self.url = "https://www.coindesk.com/price/bitcoin"

    # output magic method
    def __repr__(self):
        price = stylize(self.scrape(self.url), fg("red"))
        return f"Current Bitcoin price is: {price} $\n"

    # methods
    def scrape(self, url):
        page = requests.get(url)
        soup = BeautifulSoup(page.content, 'html.parser')
        result = soup.find(class_="price-large")
        contents = [i for i in result]

        return contents[1]

# main execution
if __name__ == "__main__":
    print(Scraper())
