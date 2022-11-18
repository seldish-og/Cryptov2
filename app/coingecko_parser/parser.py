import requests
from bs4 import BeautifulSoup


class Parser:
    def __init__(self) -> None:
        self.url = "https://www.coingecko.com/"
        self.params = {}

    def get_page_content(self):
        page = requests.get(self.url)
        return page.text

    def parse_html(self):
        page_text = self.get_page_content()
        soup = BeautifulSoup(page_text, "html.parser")
        results = soup.find_all("span", class_="lg:tw-flex")
        for i in results:
            print(i.text)


prs = Parser()


print(prs.parse_html())
