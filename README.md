# Cryptov2 Documentation

This project is a full serverside app to find crypto arbitrage pairs through different markets.
Also this app will have convinient Rest Api client.

## How to run project

1. `git clone https://github.com/seldish-og/Cryptov2.git`
2. Create and run Apache Cassandra db (for example in Docker)
   - `docker pull cassandra`
   - `docker run --name test-cassandra -e CASSANDRA_CLUSTER_NAME -p 9042:9042 -d cassandra:latest`
3. Create venv: `python -m venv venv`, start venv: `source ./venv/bin/activate`
4. Run `python ./app/database/init_db.py` to create tables in db
5.
