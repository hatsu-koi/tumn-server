from tumn import app
from tumn.resources import query, filter
from flask_restful import Api
from flask_cors import CORS

CORS(app)

api = Api(app)

api.add_resource(query.Query, '/query')
api.add_resource(filter.Filter, '/filter')
api.add_resource(filter.FilterControl, '/filter/<id>')
api.add_resource(filter.FilterInstallingStatus, '/filter/installing')
