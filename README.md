# Cryptov2 Documentation

This project is a full serverside app to find crypto arbitrage pairs through different markets.
Also this app will have convinient Rest Api client.

## Running database

### Cassandra

Run Apache Cassandra DB in Docker with your params

- `docker pull cassandra`
- `docker run --name some-cassandra -e CASSANDRA_CLUSTER_NAME -p 9042:9042 -d cassandra:latest`

### Maria DB

Run Maria DB in Docker with your params

- `docker pull mariadb`
- `docker run -d --name some-mariadb --env MARIADB_USER=user --env MARIADB_PASSWORD=pswd --env MARIADB_ROOT_PASSWORD=root_pswd -e MARIADB_DATABASE=dbmariadb -p 3306:3306 mariadb:latest`

### MySQL

Run MySQL DB in Docker with your params

- `docker pull mysql`
- `docker run -d --name some-mysql --env MYSQL_USER=user --env MYSQL_PASSWORD=pswd --env MYSQL_ROOT_PASSWORD=root_pswd -e MYSQL_DATABASE=dbmariadb -p 33060:33060 mysql:latest`

## Run project

1. `git clone https://github.com/seldish-og/Cryptov2.git`
2. Create venv: `python -m venv venv`, start venv: `source ./venv/bin/activate`
3. Create ./app/database/init_databases/.env file with your MySql settings
4. Run `python ./app/database/init_databases/init_mysql_db.py` to create tables in your MySql db
5.
