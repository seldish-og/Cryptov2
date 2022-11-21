import requests
from bs4 import BeautifulSoup

URL = "https://coinmarketcap.com/"
PARAMS = {}


def get_page_content():
    page = requests.get(URL)
    return page.text


def parse_html():
    page_text = get_page_content()
    soup = BeautifulSoup(page_text, "html.parser")
    results = soup.find_all("p", class_="ePTNty")
    for i in results:
        print(i)


print(parse_html())
