from app import db, celery
import app.models.client_db as models
from app.tasks import celery_tasks as main_celery_tasks


@celery.task()
def save_request(data):
    refer, session_token = data
    sessions = []
    for row in db.session.query(models.Session).filter_by(token=session_token):
        sessions.append(row)
    if len(sessions) > 0:
        session = sessions[0]
    else:
        session = models.Session(token=session_token)
        db.session.add(session)
        db.session.flush()
    new_request = models.Request(host=refer, session_id=session.id)
    db.session.add(new_request)
    db.session.commit()


@celery.task()
def save_session(token):
    new_session = models.Session(token=token)
    db.session.add(new_session)
    db.session.commit()
