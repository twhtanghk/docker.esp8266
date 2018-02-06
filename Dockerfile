FROM python:2

ENV APP=/root \
    NVM_DIR=/usr/local/nvm

RUN apt-get update \
&&  apt-get install -y python-pip git lua5.1 luarocks autoconf gperf flex bison texinfo gawk help2man wget libtool-bin ncurses-dev unzip vim \
&&  pip install pyserial esptool \
&&  apt-get autoremove \
&&  apt-get clean \
&&  luarocks install moonscript \
&&  (curl -o- https://raw.githubusercontent.com/creationix/nvm/v0.33.8/install.sh | bash) \
&&  . ${NVM_DIR}/nvm.sh \
&&  nvm install node \
&&  npm install yarn -g \
&&  yarn global add nodemcu-tool

WORKDIR $APP

ADD . $APP/docker.esp8266
