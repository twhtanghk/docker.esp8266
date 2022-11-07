FROM python:3

ENV APP=/root \
    NVM_DIR=${HOME}/.nvm \
    CARGO_HTTP_MULTIPLEXING=false

RUN apt-get update \
&&  apt-get install -y git lua5.1 luarocks autoconf gperf flex bison texinfo gawk help2man wget libtool-bin ncurses-dev unzip vim picocom minicom \
&&  curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh -s -- -y \
&&  . ${HOME}/.cargo/env \
&&  pip install pyserial esptool rshell \
&&  apt-get autoremove \
&&  apt-get clean \
&&  (curl -o- https://raw.githubusercontent.com/creationix/nvm/v0.33.8/install.sh | bash) \
&&  . ${NVM_DIR}/nvm.sh \
&&  nvm install node \
&&  npm install yarn -g

WORKDIR $APP

ADD . $APP/docker.esp8266
