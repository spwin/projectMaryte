import app.models.client_db
from app import db

device_network = db.Table('device_network',
                          db.Column('device_id', db.Integer, db.ForeignKey('device.id')),
                          db.Column('network_id', db.Integer, db.ForeignKey('network.id'))
                          )

from app.models.Device import Device
from app.models.Network import Network