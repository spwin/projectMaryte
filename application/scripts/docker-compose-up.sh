#!/bin/bash

((count = 100))
while [[ ${count} -ne 0 ]] ; do
    ping -c 1 database
    rc=$?
    if [[ ${rc} -eq 0 ]] ; then
        ((count = 1))
    fi
    echo 'Waiting for Database..'
    sleep 1
    ((count = count - 1))
done

if [[ ${rc} -eq 0 ]] ; then
    echo 'Starting the application!'
    if [ ! -f /var/log/gunicorn/info.log ]; then
        mkdir /var/log/gunicorn
        touch /var/log/gunicorn/info.log
    fi

    if [ ! -f /var/log/worker_flask.log ]; then
        touch /var/log/worker_flask.log
    fi

    celery -A app.celery worker -f /var/log/worker_flask.log --loglevel=info &

    gunicorn --reload --log-level=debug --log-file=- -m 007 wsgi -c /app/gunicorn.py
else
    echo 'It looks like database has not started'
fi