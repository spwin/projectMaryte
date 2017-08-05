from app import db
from app.models import device_network


class Network(db.Model):
    __tablename__ = 'network'
    id = db.Column(db.Integer, primary_key=True)
    ip = db.Column(db.String(100))

    devices = db.relationship('Device',
                              secondary=device_network,
                              backref=db.backref('device', lazy='dynamic'),
                              lazy='dynamic'
                              )

    def __init__(self, ip):
        self.ip = ip

    def serialize(self):
        row = {}
        for field in self.__table__.columns:
            row[str(field.name)] = getattr(self, str(field.name), None)
        devices = []
        for device in self.devices:
            device_data = {
                'id': device.id,
                'hash': device.hash
            }
            devices.append(device_data)
        row['devices'] = devices
        return row
