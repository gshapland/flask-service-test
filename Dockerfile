FROM ubuntu:16.04

MAINTAINER "gshapland@gamil.com"

RUN apt-get update -y && \
    apt-get install -y python-pip python-dev &&\
    mkdir /service

# We copy just the requirements.txt first to leverage Docker cache
COPY ./requirements.txt /service/requirements.txt

WORKDIR /service

RUN pip install -r requirements.txt

COPY . /service

EXPOSE 5000

ENTRYPOINT [ "python" ]

CMD [ "service.py" ]
