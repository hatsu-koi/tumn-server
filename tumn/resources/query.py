from flask_restful import reqparse, Resource
from tumn.core.filterset import FilterSet
import jpype

parser = reqparse.RequestParser()
parser.add_argument('filters', type=list, location='json')
parser.add_argument('text', type=list, location='json')


class Query(Resource):
    def post(self):
        jpype.attachThreadToJVM()
        args = parser.parse_args()
        results = {}
        sharedres = {}

        for filter in args['filters']:
            filter_object = FilterSet.filter_list[filter]
            filterset_name = filter_object.parent.name

            if filterset_name in FilterSet.sharedres_list:
                if not filterset_name in sharedres:
                    sharedres[filterset_name] = FilterSet.sharedres_list[filterset_name](args['text'])

            output = filter_object.predict(args['text'], sharedres[filterset_name])

            if len(output) > 0:
                for output_element in output:
                    if output_element[0] not in results:
                        results[output_element[0]] = []

                    results[output_element[0]].append(output_element[1])

        return list(results.items())
