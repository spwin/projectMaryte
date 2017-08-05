from app import db


class Session(db.Model):
    __tablename__ = 'session'
    __bind_key__ = 'client_db'
    id = db.Column(db.Integer, primary_key=True)
    token = db.Column(db.String(100))
    device_id = db.Column(db.Integer)

    requests = db.relationship('Request', back_populates='session')

    def __init__(self, token):
        self.token = token

    def serialize(self):
        row = {}
        for field in self.__table__.columns:
            row[str(field.name)] = getattr(self, str(field.name), None)
        requests = []
        for request in self.requests:
            request_data = {
                'id': request.id,
                'refer': request.host
            }
            requests.append(request_data)
        row['requests'] = requests
        return row
