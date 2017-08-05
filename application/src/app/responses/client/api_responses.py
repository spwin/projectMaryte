from flask import jsonify
import uuid
import sys
from flask_restful import Resource
from app.scripts import http_helper, parser, db_helper
from app.tasks import celery_tasks as main_celery_tasks
from app.tasks.client import celery_tasks as client_celery_tasks
import app.models.client_db as model


class Request(Resource):
    def get(self):
        requests = model.Request.query\
            .order_by(model.Request.id.desc())\
            .all()
        return jsonify({'Requests': db_helper.serialize(requests)})

    def post(self):
        server_data = parser.parse_user_data()
        user_data = parser.read_request_data()
        if "session" not in user_data:
            session = uuid.uuid4().hex
            client_celery_tasks.save_session.delay(str(session))
            main_celery_tasks.save_network_and_device.delay(
                server_data['X-Real-Ip'],
                user_data['hash']
            )
        else:
            session = user_data["session"]
            main_celery_tasks.save_network.delay(
                server_data['X-Real-Ip']
            )
        client_celery_tasks.save_request.delay((
            str(server_data['Referer']),
            str(session))
        )
        response = {'data': {**server_data, **user_data}, 'session': session}
        return http_helper.sendResponse(response)


class Session(Resource):
    def get(self):
        sessions = model.Session.query\
            .order_by(model.Session.id.desc())\
            .all()
        return jsonify({'Sessions': db_helper.serialize(sessions)})
