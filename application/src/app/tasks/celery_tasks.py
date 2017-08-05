from app import db, celery
import app.models as models


@celery.task()
def save_network_and_device(ip, device_hash):
    # check if exists network by ip if no add
    networks = []
    for row in db.session.query(models.Network).filter_by(ip=ip):
        networks.append(row)
    if len(networks) > 0:
        network = networks[0]
    else:
        network = models.Network(ip=ip)
        db.session.add(network)
        db.session.flush()

    # get device by hash
    devices = []
    for row in db.session.query(models.Device).filter_by(hash=device_hash):
        devices.append(row)
    if len(devices) > 0:
        device = devices[0]
    else:
        device = models.Device(hash=device_hash)
        db.session.add(device)
        db.session.flush()

    # check if network has this device if no then add
    device_exists = False
    for network_device in network.devices:
        if network_device.hash == device.hash:
            device_exists = True
    if not device_exists:
        network.devices.append(device)

    # check if device has this network if no add
    network_exists = False
    for device_network in device.networks:
        if device_network.ip == network.ip:
            network_exists = True
    if not network_exists:
        device.networksappend(network)

    db.session.commit()


@celery.task()
def save_network(ip):
    networks = []
    for row in db.session.query(models.Network).filter_by(ip=ip):
        networks.append(row)
    if len(networks) == 0:
        network = models.Network(ip=ip)
        db.session.add(network)
        db.session.commit()
