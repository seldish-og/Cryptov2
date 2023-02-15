import json
import cchardet
import lxml
import requests
from bs4 import BeautifulSoup


def write_json(data: dict):
    with open('./files/json_data.json', 'w') as outfile:
        json.dump(data, outfile)


class DataFormatter:
    def format_string_tags(self, all_tags):
        strings = []
        for i in all_tags:
            strings.append(str(i.text.strip()))
        return strings

    def format_int_tags(self, all_tags):
        digits = []
        for i in all_tags:
            digits.append(
                int(i.text.strip().replace("$", "").replace(",", "").replace(".", "")))
        return digits


class Parser(DataFormatter):
    def __init__(self) -> None:
        self.url = "https://www.coingecko.com/"
        self.params = {}

    def get_page_content(self):
        page = requests.get(self.url)
        return page.text

    def get_html_data(self):
        page_text = self.get_page_content()
        soup = BeautifulSoup(page_text, "lxml")

        all_crypto_names = soup.find_all("span", class_="lg:tw-flex")
        crypto_names = self.format_string_tags(all_tags=all_crypto_names)

        all_crypto_symbols = soup.find_all("span", class_="d-lg-inline")
        crypto_symbols = self.format_string_tags(all_tags=all_crypto_symbols)

        all_day_volume = soup.find_all("td", class_="td-liquidity_score")
        day_volume = self.format_int_tags(all_tags=all_day_volume)

        all_market_cap = soup.find_all("td", class_="td-market_cap")
        market_cap = self.format_int_tags(all_tags=all_market_cap)

        return crypto_names, crypto_symbols, day_volume, market_cap


parser = Parser()
# print(prs.get_html_data())


def check_and_save_data():
    crypto_names, crypto_symbols, day_volume, market_cap = parser.get_html_data()

    result_dict = {}
    for value_index, value in enumerate(day_volume):
        if value > 1000000:
            result_dict[crypto_names[value_index]] = [
                crypto_symbols[value_index], value, market_cap[value_index]]
    write_json(result_dict)


check_and_save_data()
