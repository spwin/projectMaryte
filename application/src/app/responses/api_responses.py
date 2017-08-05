from flask import jsonify
from flask_restful import Resource
from app.scripts import http_helper, parser, db_helper
import app.models as model


class Network(Resource):
    def get(self):
        networks = model.Network.query\
            .order_by(model.Network.id.desc())\
            .all()
        return jsonify({'Networks': db_helper.serialize(networks)})


class Device(Resource):
    def get(self):
        devices = model.Device.query\
            .order_by(model.Device.id.desc())\
            .all()
        return jsonify({'Devices': db_helper.serialize(devices)})
