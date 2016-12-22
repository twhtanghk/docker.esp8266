# docker.esp8266
Dockerfile to create image with git, python, nodejs, coffeescript, lua, luarocks, moonscript, minicom, esptool, luatool, NodeMCU-Tool for esp8266 programming

## start container
```
docker run -it --device /dev/ttyUSB0 twhtanghk/docker.esp8266
```

## flash firmware
browse https://nodemcu-build.com/index.php
enable required modules (e.g. adc, cjson, end user setup, file, gpio, net, node, timer, wifi)
```
~/esptool/esptool.py write_flash 0x00000 nodemcu-xxxx.bin
```

## compile, mkfs, or upload
```
cd ~/src
moonc *.moon
nodemcu-tool mkfs
nodemcu-tool upload *.lua
```
