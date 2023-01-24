import json
import requests
from bs4 import BeautifulSoup


def write_json(data: dict):
    with open('./files/json_data.json', 'w') as outfile:
        json.dump(data, outfile)


class DataFormatter:
    def format_strings(self, all_tags):
        strings = []
        for i in all_tags:
            strings.append(str(i.text.strip()))
        return strings

    def format_digits(self, all_tags):
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
        soup = BeautifulSoup(page_text, "html.parser")

        all_crypto_names = soup.find_all("span", class_="lg:tw-flex")
        crypto_names = self.format_strings(all_tags=all_crypto_names)

        all_crypto_symbols = soup.find_all("span", class_="lg:tw-flex")
        crypto_symbols = self.format_strings(all_tags=all_crypto_names)

        all_day_volume = soup.find_all("td", class_="td-liquidity_score")
        day_volume = self.format_digits(all_tags=all_day_volume)

        all_market_cap = soup.find_all("td", class_="td-market_cap")
        market_cap = self.format_digits(all_tags=all_market_cap)

        return crypto_names, len(crypto_names)


prs = Parser()
print(prs.get_html_data())


def prepare_parsed_data_to_save():
    crypto_names, day_volume, market_cap = prs.get_html_data()
    result_dict = {}
    for value in day_volume:
        if int(value.text) > 1000000:
            value_index = day_volume.index(value)
            result_dict[crypto_names[value_index]] = [
                value, market_cap[value_index]]
    write_json(result_dict)


# prepare_parsed_data_to_save()
