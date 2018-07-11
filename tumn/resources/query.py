from flask_restful import reqparse, Resource
from tumn.core.filterset import FilterSet

parser = reqparse.RequestParser()
parser.add_argument('filters', type=list, location='json')
parser.add_argument('text', type=list, location='json')


class Query(Resource):
    def post(self):
        args = parser.parse_args()
        results = []

        for filter in args['filters']:
            filter_object = FilterSet.filters[filter]
            results.append(*filter_object.predict(args['text']))


        return results
