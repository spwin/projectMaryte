FROM nginx:1.13.3-alpine
MAINTAINER spwin
RUN apk --update add bash

ADD ./scripts /scripts/nginx/

RUN chmod +x /scripts/nginx/docker-compose-up.sh
CMD /scripts/nginx/docker-compose-up.sh