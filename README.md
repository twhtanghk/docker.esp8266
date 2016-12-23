# docker.esp8266
Dockerfile to create image with git, python, nodejs, coffeescript, lua, luarocks, moonscript, minicom, esptool, luatool, NodeMCU-Tool for esp8266 programming

## start container
```
docker run -it --device /dev/ttyUSB0 twhtanghk/docker.esp8266
```

## nodemcu
### flash firmware
browse https://nodemcu-build.com/index.php
enable required modules (e.g. adc, cjson, end user setup, file, gpio, net, node, timer, wifi)
```
~/esptool/esptool.py write_flash 0x00000 nodemcu-xxxx.bin
```

### compile, mkfs, or upload
```
cd ~/src
moonc *.moon
nodemcu-tool mkfs
nodemcu-tool upload *.lua
```

## espruino
### flash firmware
```
# compile esp-open-sdk
cd ~/esp-open-sdk
make

# define env vars for compiling espruino
export ESP8266_BOARD=1
export FLASH_4MB=1
export ESP8266_SDK_ROOT=/home/user/esp-open-sdk/ESP8266_NONOS_SDK_XXXXXXX
export ESPTOOL=/home/user/esp-open-sdk/esptool/esptool.py
export COMPORT=/dev/ttyUSB0
export PATH=$PATH:/home/esp-open-sdk/xtensa-lx106-elf/bin/

# compile espruino
cd ~/Espruino
make

# flash connected device
make flash
```

### compile coffeescript
```
cd ~/coffee
npm install
node_modules/.bin/gulp
```
