from cassandra.cluster import Cluster


cluster = Cluster()


def create_keyspace():
    session = cluster.connect()
    session.execute('''
    create keyspace pairskeyspace with replication={
    'class': 'SimpleStrategy', 'replication_factor' : 1
    };
    ''')


def create_table():
    session = cluster.connect('pairskeyspace')
    create_db_qry = '''
    CREATE TABLE testssrt (id int PRIMARY_KEY, name text);
    '''
    session.execute(create_db_qry)
