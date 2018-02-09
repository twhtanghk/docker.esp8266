#!/bin/sh

cmd='rshell -p /dev/ttyUSB0 --buffer-size 100'

find dist -name \*.map -exec rm {} \;
$cmd rm -rf /pyboard/static/*
$cmd rsync dist/ /pyboard/static
