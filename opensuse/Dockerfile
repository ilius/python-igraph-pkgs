FROM debian:sid
MAINTAINER Saeed Rasooli saeed.gnu@gmail.com
LABEL Description="Simple Docker image that contains a pre-compiled version of igraph's Python interface"

RUN zypper refresh
RUN apt-get -y install build-essential libxml2-dev zlib1g-dev pkg-config libffi-dev libcairo-dev
RUN apt-get -y install python3-dev
RUN apt-get -y install python3-pip
RUN pip3 install python-igraph

RUN zypper -y install rpm-build

RUN mkdir -p /root/build
RUN cd /root/build/

CMD /bin/bash
