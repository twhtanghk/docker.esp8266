#!/bin/sh

rshell -a -b 115200 --buffer-size=100 -p /dev/ttyS2 <<EOF
rm -rf /pyboard/*
cp boot.py main.py config.json project.mpy config.mpy log.mpy sta.mpy ap.mpy gpio.mpy /pyboard
cp $HOME/src/microdot/src/microdot.mpy /pyboard
EOF
