import base64
import json
import simplejson
from flask import Response, send_file


def sendResponse(data):
    resp = Response(json.dumps(data))
    resp.headers['Access-Control-Allow-Origin'] = '*'
    return resp


def sendFile(filename, ftype='', folder='static', mime=''):
    path = folder + '/' + (ftype + '/' if ftype else '') + filename
    if ftype == 'images':
        return sendImage(path, mime=mime)


def sendImage(path, mime):
    return send_file(path, mimetype=mime)


def decodeBase64(encoded, json=False):
    decoded = base64.b64decode(encoded)
    return simplejson.loads(decoded) if json else decoded.decode('ascii')
