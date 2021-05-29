FROM alpine:3.13

USER root

RUN apk update
RUN apk add python3 py3-pip

RUN adduser -h /home/dbfinal -D dbfinal
RUN chown -R dbfinal:dbfinal /home/dbfinal
RUN chmod -R 755 /home/dbfinal
USER dbfinal:dbfinal

WORKDIR /home/dbfinal/workdir
COPY requirements.txt .
RUN pip install -r requirements.txt

CMD ["python3", "-m", "backend"]
