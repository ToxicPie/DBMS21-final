# DBMS Final Project

## Setting up

This project uses docker and docker-compose for its services, so first make sure you have them installed.

Copy `flask_config-example.py` to `frontend/flask_config.py` and `backend/flask_config.py` respectively. You might want to edit their contents, for example, setting `DEBUG = True` in a development environment.

Then, copy `mariadb-example.env` to `mariadb.env`. This file contains MariaDB credentials, so you should edit the contents.

To start a production server, run:
```sh
docker-compose build
docker-compose up
```

To start a development server, first switch to the development branch by `git checkout development`, then the commands above.
