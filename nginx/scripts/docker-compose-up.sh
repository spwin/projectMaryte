#!/bin/bash

until [ -e /var/run/sockets/app.sock ]; do
  echo 'Waiting for Gunicorn socket..'
  sleep 2
done

chmod 776 /var/run/sockets/app.sock

nginx -g 'daemon off;'

tail -f /var/log/nginx/error.log