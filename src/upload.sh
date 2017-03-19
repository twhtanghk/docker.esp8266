#!/bin/sh

nodemcu-tool mkfs
prog=""
for i in init app wlan req res log router middleware controller str; do
  prog="${prog} $i.lua"
done
nodemcu-tool upload ${prog}
