FROM ubuntu:latest

ENV DEBIAN_FRONTEND=noninteractive

ENV TZ=UTC
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

RUN apt-get update -y
RUN apt-get upgrade -y

RUN apt-get install -y \
    curl \
    htop \
    iputils-ping \
    nmap \
    telnet \
    tmux \
    vim \
    wget
