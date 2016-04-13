FROM python:2
RUN apt-get update && \
	apt-get install git lua5.2 && \
	apt-get clean && \
	cd ${HOME} && \
	git clone https://github.com/themadinventor/esptool && \
	git clone https://github.com/4refr0nt/luatool.git && \
ENTRYPOINT /bin/bash