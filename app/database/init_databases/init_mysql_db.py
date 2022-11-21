import os
import sys
import mysql.connector
from dotenv import load_dotenv

load_dotenv()

mysql_user = os.environ.get("mysql_user")
mysql_password = os.environ.get("mysql_password")
mysql_host = os.environ.get("mysql_host")
mysql_port = os.environ.get("mysql_port")
mysql_database = os.environ.get("mysql_database")
print(mysql_port)

connection = mysql.connector.connect(
    user=mysql_user,
    password=mysql_password,
    host=mysql_host,
    port=(mysql_port),
    database=mysql_database)

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
            id int NOT NULL AUTO_INCREMENT,
            symbol text NOT NULL,
            coin_name text NOT NULL,
            withdrawal_fee int,
            buy_sell_fee int,
            min_withdrawal int,
            max_withdrawal int,
            primary key(id)
            );'''
        cursor.execute(create_market_fees_db_qry)


if __name__ == "__main__":
    create_coins_tables(cursor)
    create_markets_fees_tables(cursor)
    connection.commit()
    connection.close()
