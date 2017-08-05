from app import db


class Request(db.Model):
    __tablename__ = 'request'
    __bind_key__ = 'client_db'
    id = db.Column(db.Integer, primary_key=True)
    host = db.Column(db.String(10000))
    session_id = db.Column(db.Integer, db.ForeignKey('session.id'))

    session = db.relationship('Session', foreign_keys=session_id)

    def __init__(self, host, session_id):
        self.host = host
        self.session_id = session_id

    def serialize(self):
        row = {}
        for field in self.__table__.columns:
            row[str(field.name)] = getattr(self, str(field.name), None)
        return row
