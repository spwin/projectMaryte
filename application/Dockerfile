FROM python:3.6.2-alpine
MAINTAINER spwin
RUN apk --update add bash


ENV APP_DIR /app
WORKDIR $APP_DIR

ADD ./src $APP_DIR
ADD ./scripts /scripts/app/


#RUN apk add alpine-sdk=0.4-r3
RUN apk add gcc=5.3.0-r0
RUN apk add libc-dev=0.7-r0
#RUN apk add fortify-headers=0.8-r0
RUN apk add mariadb-dev=10.1.22-r0
RUN pip install -r requirements.txt

RUN chmod +x /scripts/app/docker-compose-up.sh

CMD /scripts/app/docker-compose-up.sh