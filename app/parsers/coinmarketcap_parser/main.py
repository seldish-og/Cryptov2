import json

x = {
    "1": {
        "bitcoin": "btc",
        "24h market cap": "20202$",
        "markets": ["Binance", "Huobi"]
    },
    "2": {
        "etherium": "eth",
        "24h market cap": "12345$",
        "markets": ["BuyBit", "Huobi"]
    },

}

with open("./files/test.json", "w", encoding="UTF-8") as file:
    file.write(json.dumps(x))
