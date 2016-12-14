FROM python:2

ENV VER=${VER:-master} \
    REPO=https://github.com/twhtanghk/docker.esp8266 \
    APP=/usr/src/app

WORKDIR /root

RUN curl -sL https://deb.nodesource.com/setup_4.x | bash - && \
    apt-get update && \
    apt-get -y install git lua5.1 luarocks minicom nodejs && \
    apt-get -y autoremove && \
    apt-get clean && \
    git clone ${REPO} ${APP} && \
    mv ${APP}/.git* ${APP}/* /root && \
    luarocks install moonscript && \
    npm install coffee-script nodemcu-tool -g && \
    pip install pyserial && \
    git clone https://github.com/themadinventor/esptool && \
    git clone https://github.com/4refr0nt/luatool.git

ENTRYPOINT top -b -d 100
