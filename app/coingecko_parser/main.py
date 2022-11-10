'''After runing script.sh we get .json file which we can parse '''
import json
from pprint import pprint


def open_json():
    with open("./files/full_list.json", mode="r", encoding="UTF-8") as file:
        json_file = json.load(file)
    return json_file


json_file = open_json()
final_json = {}
for i in json_file:
    if i['total_volume'] > 1000000:
        final_json[i['symbol']] = f"{i['total_volume']}$"

pprint(final_json)
