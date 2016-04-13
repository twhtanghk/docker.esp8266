# docker.esp8266
Dockerfile to create image with git, python, lua, luarocks, moonscript, minicom, esptool, luatool for esp8266 programming

## start container
```
docker run -it --device /dev/ttyUSB0 twhtanghk/docker.esp8266
```