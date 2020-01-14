FROM python:3.7
LABEL MAINTAINER Alexandr.Trushnikov <kimp1er@gmail.com>
LABEL SERVICE scrapy-rutracker

ADD ./rutracker /app/
ADD ./requirements.txt /app/
RUN apt update && apt install -yq \
      python-dev \
      python3-pip
RUN pip3 install -r /app/requirements.txt

WORKDIR /app/rutracker

