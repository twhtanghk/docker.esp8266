FROM python:2
WORKDIR ${HOME}
RUN curl -sL https://deb.nodesource.com/setup_4.x | bash - && \
	apt-get update && \
	apt-get -y install git lua5.1 luarocks minicom nodejs && \
	apt-get -y autoremove && \
	apt-get clean && \
	cd ${HOME} && \
	wget -q -O /etc/minicom/minirc.dfl https://raw.githubusercontent.com/twhtanghk/docker.esp8266/master/minirc.dfl && \
	luarocks install moonscript && \
	npm install coffee-script nodemcu-tool -g && \
	pip install pyserial && \
	git clone https://github.com/themadinventor/esptool && \
	git clone https://github.com/4refr0nt/luatool.git
ENTRYPOINT /usr/bin/top -b -d 100