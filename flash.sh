#!/bin/sh

rshell -a -b 115200 --buffer-size=100 -p /dev/ttyUSB0 <<EOF
rm -rf /pyboard/*
mkdir /pyboard/static
rsync -v frontend/dist /pyboard/static
rsync -v esp8266 /pyboard
EOF
