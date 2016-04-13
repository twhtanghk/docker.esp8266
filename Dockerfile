FROM python:2
WORKDIR ${HOME}
RUN apt-get update && \
	apt-get -y install git lua5.2 && \
	apt-get -y autoremove && \
	apt-get clean && \
	cd ${HOME} && \
	git clone https://github.com/themadinventor/esptool && \
	git clone https://github.com/4refr0nt/luatool.git
ENTRYPOINT /bin/bash