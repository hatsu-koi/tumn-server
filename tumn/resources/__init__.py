from tumn import app
from tumn.resources.query import Query
from tumn.resources.filterset.index import FilterSetManager
from tumn.core.filterset import FilterSet
from flask_restful import Api
from flask_cors import CORS

CORS(app)

api = Api(app)

api.add_resource(Query, "/query")
api.add_resource(FilterSetManager, "/filterset/", "/filterset/<id_>/")

FilterSet.load_filters()
