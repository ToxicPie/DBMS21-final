FROM alpine:3.13

USER root

RUN apk update
RUN apk add musl-dev python3-dev gcc
RUN apk add python3 py3-pip uwsgi-python3 mariadb-connector-c-dev

WORKDIR /workdir

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY uwsgi.ini .
CMD ["uwsgi", "--ini", "uwsgi.ini"]
