# docker.esp8266
Dockerfile to create image with git, python, nodejs, coffeescript, lua, luarocks, moonscript, minicom, esptool, luatool, NodeMCU-Tool for esp8266 programming

## start container
```
docker run -it --device /dev/ttyUSB0 twhtanghk/docker.esp8266
```

## flash firmware
```
/root/esptool/esptool.py ...
```

## compile, mkfs, or upload
```
cd /root/src
moonc *.moon
nodemcu-tool mkfs
nodemcu-tool upload *.lua
```