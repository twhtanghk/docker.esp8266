#!/bin/sh

nodemcu-tool mkfs
prog="init config wlan telnet http app req res log router middleware controller str motor"
moon=""
lua=""
lc=""
for i in ${prog}; do
  moon="${moon} $i.moon"
  lua="${lua} $i.lua"
  lc="${lc} $i.lc"
  moonc $i.moon
  luac -o $i.lc $i.lua
done
nodemcu-tool upload ${lua} data.json
