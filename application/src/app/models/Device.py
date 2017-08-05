from app import db
from app.models import device_network


class Device(db.Model):
    __tablename__ = 'device'
    id = db.Column(db.Integer, primary_key=True)
    hash = db.Column(db.String(100))

    networks = db.relationship('Network',
                               secondary=device_network,
                               backref=db.backref('network', lazy='dynamic'),
                               lazy='dynamic'
                               )

    def __init__(self, hash):
        self.hash = hash

    def serialize(self):
        row = {}
        for field in self.__table__.columns:
            row[str(field.name)] = getattr(self, str(field.name), None)
        networks = []
        for network in self.networks:
            network_data = {
                'id': network.id,
                'IP': network.ip
            }
            networks.append(network_data)
        row['networks'] = networks
        return row
