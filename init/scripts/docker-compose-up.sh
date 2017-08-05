#!/bin/bash

connected=false
host='elasticsearch:9200'

while [ "$connected" = false ]; do
    status=$(curl -s -u elastic:changeme -o /dev/null -I -w "%{http_code}" http://"${host}"/)
    if [ ! ${status} == "200" ] && [ ! ${status} == "304" ]  && [ ! ${status} == "302" ]; then
        echo ${status} + 'Waiting for connection to elasticsearch..'
    else
        curl -XPUT 'http://'"${host}"'/_xpack/license?acknowledge=true' -H "Content-Type: application/json" -d @scripts/license.json
        connected=true
    fi
    sleep 4
done