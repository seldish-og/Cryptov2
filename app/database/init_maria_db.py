import os
import sys
import mariadb
from dotenv import load_dotenv

load_dotenv()

maria_user = os.environ.get("maria_user")
maria_password = os.environ.get("maria_password")
maria_host = os.environ.get("maria_host")
maria_port = os.environ.get("maria_port")
maria_database = os.environ.get("maria_database")


connection = mariadb.connect(
    user=maria_user,
    password=maria_password,
    host=maria_host,
    port=int(maria_port),
    database=maria_database)

cursor = connection.cursor()


def create_coins_tables(cursor):
    create_coins_db_qry = '''
    CREATE TABLE Coins (
        id INT NOT NULL AUTO_INCREMENT,
        symbol text NOT NULL,
        coin_name text NOT NULL,
        day_volume int NOT NULL,
        market_cap int NOT NULL,
        markets json, 
        PRIMARY KEY(id)
        );'''
    cursor.execute(create_coins_db_qry)


def create_markets_fees_tables(cursor):
    markets = ["huobi", "bitget", "mexc", "bybit", "kucoin", "gateio"]

    for market in markets:
        create_market_fees_db_qry = f'''
        CREATE TABLE {market}_fees (
            id int,
            symbol text,
            coin_name text,
            withdrawal_fee int,
            buy_sell_fee int,
            min_withdrawal int,
            max_withdrawal int,
            primary key(id)
            );'''
        cursor.execute(create_market_fees_db_qry)


if __name__ == "__main__":
    create_coins_tables(cursor)
    # create_markets_fees_tables(cursor)
    connection.commit()
    connection.close()
