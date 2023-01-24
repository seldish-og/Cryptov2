import json
import requests
from bs4 import BeautifulSoup


def write_json(data: dict):
    with open('./files/json_data.json', 'w') as outfile:
        json.dump(data, outfile)


class Parser:
    def __init__(self) -> None:
        self.url = "https://www.coingecko.com/"
        self.params = {}

    def get_page_content(self):
        page = requests.get(self.url)
        return page.text

    def get_html_data(self):
        page_text = self.get_page_content()
        soup = BeautifulSoup(page_text, "html.parser")
        # crypto_names = soup.find_all("span", class_="lg:tw-flex")
        day_volume = []
        for i in soup.find_all("td", class_="td-liquidity_score"):
            day_volume.append(
                int(i.text.strip().replace("$", "").replace(",", "").replace(".", "")))

        # market_cap = soup.find_all("td", class_="td-market_cap")
        return day_volume, len(day_volume)


prs = Parser()
print(prs.get_html_data())


# def prepare_parsed_data_to_save():
#     crypto_names, day_volume, market_cap = prs.get_html_data()
#     result_dict = {}
#     for value in day_volume:
#         if int(value.text) > 1000000:
#             value_index = day_volume.index(value)
#             result_dict[crypto_names[value_index]] = [
#                 value, market_cap[value_index]]
#     write_json(result_dict)


# prepare_parsed_data_to_save()
