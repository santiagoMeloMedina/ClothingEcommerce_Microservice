
FROM python:3.6
WORKDIR /usr/src/app
COPY . /usr/src/app
RUN apt-get update && apt-get install jq vim nano curl -y
RUN pip3 install -r requisites.info
STOPSIGNAL SIGINT
CMD ["uwsgi", "src/product.ini"]