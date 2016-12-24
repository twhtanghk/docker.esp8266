FROM python:2

ENV VER=${VER:-master} \
    REPO=https://github.com/twhtanghk/docker.esp8266 \
    APP=/usr/src/app \
    NPM_CONFIG_LOGLEVEL=info \
    NODE_VERSION=7.3.0

RUN useradd -ms /bin/bash -G dialout user && \
    pip install pyserial && \
    apt-get update && \
    apt-get install -y git lua5.1 luarocks autoconf gperf flex bison texinfo gawk help2man wget libtool-bin ncurses-dev unzip vim && \
    apt-get autoremove && \
    apt-get clean && \
    luarocks install moonscript && \
    curl -SLO "https://nodejs.org/dist/v$NODE_VERSION/node-v$NODE_VERSION-linux-x64.tar.xz" && \
    tar -xJf "node-v$NODE_VERSION-linux-x64.tar.xz" -C /usr/local --strip-components=1 && \
    ln -s /usr/local/bin/node /usr/local/bin/nodejs && \
    npm install coffee-script nodemcu-tool -g

USER user
WORKDIR /home/user

RUN git clone ${REPO} && \
    git clone https://github.com/espruino/Espruino && \
    git clone --recursive https://github.com/pfalcon/esp-open-sdk.git && \
    git clone https://github.com/4refr0nt/luatool.git && \
    (cd esp-open-sdk; make)

ENTRYPOINT top -b -d 100
