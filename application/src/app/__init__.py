from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api

app = Flask(__name__, instance_relative_config=True)
app.config.from_object('app.config.DevelopmentConfig')
api = Api(app)
db = SQLAlchemy(app)

from app import worker
celery = worker.make_celery(app)

import app.models as models
db.create_all()

from app import routes
