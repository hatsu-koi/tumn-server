from tumn import app
from flask_restful import Api
from flask_cors import CORS
from tumn.resources.query import Query

CORS(app)

api = Api(app)

api.add_resource(Query, '/query')
