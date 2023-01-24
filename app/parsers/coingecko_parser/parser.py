import json
import requests
from bs4 import BeautifulSoup


def write_json(data: dict):
    with open('./files/json_data.json', 'w') as outfile:
        json.dump(data, outfile)


class DataFormatter:
    def prepare_crypto_names(self):
        pass

    def prepare_market_cap(self):
        pass

    def prepare_day_volume(self, all_tags):
        day_volume = []
        for i in all_tags:
            day_volume.append(
                int(i.text.strip().replace("$", "").replace(",", "").replace(".", "")))
        return day_volume


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

        crypto_names = soup.find_all("span", class_="lg:tw-flex")

        # all_day_volume = soup.find_all("td", class_="td-liquidity_score")
        # day_volume = self.prepare_day_volume(all_tags=all_day_volume)

        all_market_cap = soup.find_all("td", class_="td-market_cap")
        market_cap = self.prepare_day_volume(all_tags=all_market_cap)

        return market_cap, len(market_cap)


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
