FROM alpine:3.6
RUN apk --update add bash
RUN apk add curl
# ENV ES_JAVA_OPTS="-Des.path.conf=/etc/elasticsearch"
# ENV ES_USERNAME=unicorn
# ENV ES_PASSWORD=qdaews321
# ENV ELASTICSEARCH_USER="unicorn"
# ENV ELASTICSEARCH_PASS="qdaews321"
# ENV UID_TO_SET="88"

# RUN echo "elasticsearch:x:$UID_TO_SET:$UID_TO_SET::/home/elasticsearch:" >> /etc/passwd

# RUN echo "elasticsearch:!:$(($(date +%s) / 60 / 60 / 24)):0:99999:7:::" >> /etc/shadow
# RUN echo "elasticsearch:x:$UID_TO_SET:" >> /etc/group
# RUN mkdir /home/elasticsearch
# RUN chown user: /home/elasticsearch

# RUN su elasticsearch

# RUN echo test 0 > /tmp/test0

# CMD elasticsearch -E network.host=0.0.0.0 -E discovery.zen.minimum_master_nodes=1

ADD ./scripts /scripts/
RUN chmod a+x /scripts/docker-compose-up.sh

# CMD tail -f /bin/bash
# USER elasticsearch
CMD /scripts/docker-compose-up.sh
# CMD elasticsearch -E network.host=0.0.0.0 -E discovery.zen.minimum_master_nodes=1