from cassandra.cluster import Cluster


cluster = Cluster()


def create_keyspace():
    session = cluster.connect()
    session.execute('''
    create keyspace pairskeyspace with replication={
    'class': 'SimpleStrategy', 'replication_factor' : 1
    };
    ''')


def create_coins_tables(session):
    create_coins_db_qry = '''
    CREATE TABLE coins (
        id int,
        symbol text,
        coin_name text,
        day_volume int,
        markets list<int>, 
        primary key(id)
        );'''
    session.execute(create_coins_db_qry)


def create_markets_fees_tables(session):
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
        session.execute(create_market_fees_db_qry)


if __name__ == "__main__":
    create_keyspace()
    session = cluster.connect('pairskeyspace')
    create_coins_tables(session)
    create_markets_fees_tables(session)
