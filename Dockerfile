FROM python:3.7
LABEL MAINTAINER Alexandr.Trushnikov <kimp1er@gmail.com>
LABEL SERVICE scrapy-rutracker

RUN apt update && apt install -yq \
      python-dev \
      python3-pip

ADD ./requirements.txt /app/
RUN pip3 install -r /app/requirements.txt
ADD . /app/

WORKDIR /app/rutracker
CMD './spider_entrypoint.sh'

