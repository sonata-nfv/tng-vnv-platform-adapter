FROM ubuntu:latest
MAINTAINER Aureliano Sinatra "aureliano.sinatra@easyglobalmarket.com"
RUN apt-get update -y && apt-get install -y python3 python3-dev python3-pip curl python-pip libcurl4-gnutls-dev libgnutls28-dev git libpq-dev
COPY ./requirements.txt /app/requirements.txt
WORKDIR /app
RUN pip3 install -r requirements.txt
RUN pip3 install -U Flask_Cors

COPY . /app
RUN export LC_ALL="en_US.UTF-8"
RUN export LC_CTYPE="en_US.UTF-8"

EXPOSE 5001
CMD ["python3", "/app/main.py"]
