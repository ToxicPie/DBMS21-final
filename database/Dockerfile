FROM mariadb:focal

USER mysql
WORKDIR /var/lib/mysql

COPY mariadb-init /docker-entrypoint-initdb.d
COPY csv ./csv
