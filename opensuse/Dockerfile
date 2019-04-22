FROM opensuse/leap
MAINTAINER Saeed Rasooli saeed.gnu@gmail.com
LABEL Description="Simple Docker image that contains a pre-compiled version of igraph's Python interface"

RUN zypper refresh

# build-essential

RUN zypper install -y libxml2-devel zlib-devel pkg-config libffi-devel
RUN zypper install -y cairo-devel
RUN zypper install -y python3-devel
RUN zypper install -y python3-pip
RUN zypper install -y rpm-build
RUN zypper install -y gcc-c++
RUN zypper install -y make

RUN pip3 install python-igraph



RUN mkdir -p /root/build
RUN cd /root/build/

CMD /bin/bash
