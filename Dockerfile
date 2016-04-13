FROM python:2
WORKDIR ${HOME}
RUN apt-get update && \
	apt-get -y install git lua5.2 luarocks minicom && \
	apt-get -y autoremove && \
	apt-get clean && \
	cd ${HOME} && \
	wget -q -O /etc/minicom/minirc.dfl https://raw.githubusercontent.com/twhtanghk/docker.esp8266/master/minirc.dfl && \
	luarocks install moonscript && \
	pip install pyserial && \
	git clone https://github.com/themadinventor/esptool && \
	git clone https://github.com/4refr0nt/luatool.git
ENTRYPOINT /bin/bash