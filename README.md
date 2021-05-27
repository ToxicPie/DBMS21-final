# DBMS Final Project

## Setting up

This project uses docker and docker-compose for its services, so first make sure you have them installed.

Copy `flask_config-example.py` to `frontend/flask_config.py` and `backend/flask_config.py` respectively. You might want to edit their contents, for example, setting `DEBUG = True` in a development environment.

To start a production server, run:
```sh
docker-compose build
docker-compose up
```

To start a development server, run:
```sh
docker-compose -f docker-compose-dev.yml build
docker-compose -f docker-compose-dev.yml up
```
