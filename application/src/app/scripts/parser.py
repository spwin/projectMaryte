from flask import request
from app.scripts import http_helper


def parse_user_data():
    data = dict()
    for key, value in request.headers:
        data[key] = value
    return data


def read_request_data():
    normalized = dict()
    user_data = request.form.get('user_data')
    if user_data is not None:
        arguments = http_helper.decodeBase64(encoded=user_data, json=True)
        for item in arguments:
            normalized[item['key']] = item['value']
    device_hash = request.form.get('hash')
    if device_hash is not None:
        normalized['hash'] = http_helper.decodeBase64(encoded=device_hash)
    session = request.form.get('session')
    if session is not None:
        normalized['session'] = http_helper.decodeBase64(encoded=session)
    return normalized
