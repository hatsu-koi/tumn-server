from flask_restful import reqparse, Resource
from tumn.core.filterset import FilterSet

parser = reqparse.RequestParser()
parser.add_argument('filters', type=list, location='json')
parser.add_argument('text', type=list, location='json')


class Query(Resource):
    def post(self):
        args = parser.parse_args()
        results = []
        sharedres = {}

        for filter in args['filters']:
            filter_object = FilterSet.filter_list[filter]
            filterset_name = filter_object.parent.name

            if filterset_name in FilterSet.sharedres_list:
                if not filterset_name in sharedres:
                    sharedres[filterset_name] = FilterSet.sharedres_list[filterset_name](args['text'])

            output = filter_object.predict(args['text'], sharedres[filterset_name])

            if len(output) > 0:
                results.append(*output)

        return results
