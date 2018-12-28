#!/bin/sh

rshell -a -b 115200 --buffer-size=100 -p /dev/ttyUSB0 <<EOF
rm -rf /pyboard/*
mkdir /pyboard/static
rsync -v $HOME/docker.esp8266/frontend/dist /pyboard/static
rsync -v $HOME/docker.esp8266/python /pyboard
rsync -v $HOME/.micropython /pyboard
EOF
