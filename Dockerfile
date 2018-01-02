FROM node

ENV APP=/home/user

RUN apt-get update && \
    apt-get install -y python-pip git lua5.1 luarocks autoconf gperf flex bison texinfo gawk help2man wget libtool-bin ncurses-dev unzip vim && \
    useradd -ms /bin/bash -G dialout user && \
    chown user.user $APP && \
    pip install pyserial esptool && \
    apt-get autoremove && \
    apt-get clean && \
    luarocks install moonscript && \
    yarn global add nodemcu-tool

WORKDIR $APP
USER user

ADD . $APP/docker.esp8266
