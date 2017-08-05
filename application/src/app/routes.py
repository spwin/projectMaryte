from app import app, api
from app.responses import api_responses as main_resp
from app.responses.client import api_responses as client_resp


url = '/api/' + app.config.get('API_VERSION')

# Main
api.add_resource(main_resp.Device, url + '/device')
api.add_resource(main_resp.Network, url + '/network')

# Client
api.add_resource(client_resp.Request, url + '/request')
api.add_resource(client_resp.Session, url + '/session')
