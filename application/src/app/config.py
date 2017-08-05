import os
basedir = os.path.abspath(os.path.dirname(__file__))


class BaseConfig(object):
    WTF_CSRF_ENABLED = True
    SECRET_KEY = 'you-will-never-guess'
    API_VERSION = 'v1.0'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = "mysql://unicorn:qdaews321@database:3306/db_flask"
    SQLALCHEMY_BINDS = {
        'client_db': 'mysql://client:qdaews321@client_db:3307/db_client'
    }
    SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'repository')
    CELERY_BROKER_URL = 'amqp://admin:mypass@rabbit:5672'
    CELERY_RESULT_BACKEND = 'rpc://'


class DevelopmentConfig(BaseConfig):
    DEBUG = True


class ProductionConfig(BaseConfig):
    DEBUG = False
