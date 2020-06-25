FROM ubuntu:18.04


RUN apt-get update \
      && apt-get install -y \
      python-dev

ARG my_ver=1.0
ARG MY_CMD=ls
WORKDIR /root
COPY hello.py .
COPY cmd.sh .
ENV my_ver $my_ver
ENV MY_CMD $MY_CMD

ENTRYPOINT ["bash", "./cmd.sh"]