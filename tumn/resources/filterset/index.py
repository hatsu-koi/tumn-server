from flask_restful import reqparse, Resource
from tumn.core.filterset import FilterSet
import os

parser = reqparse.RequestParser()
parser.add_argument('url', location='json')
parser.add_argument('target', location='args')


class FilterSetMessage(Resource):
    def get(self):
        return {'message': '\n'.join(FilterSet.message_queue.join())}


class FilterSetManager(Resource):
    def get(self):
        return {
            'filters': [FilterSet.read_metadata(f) for f in FilterSet.filterset_paths()],
            'messages': FilterSet.pop_messages()
        }

    def post(self):
        args = parser.parse_args()

        name = os.path.basename('filterset').replace('.git', '')
        filterset = FilterSet(name)

        FilterSet.download_filter(args['url'])
        FilterSet.push_message('FilterSet download complete. Loading FilterSet...')

        filterset.load()

    def delete(self, id_):
        try:
            FilterSet.delete_filterset(id_)
        except KeyError:
            return {
                'success': False,
                'message': 'Filterset not found.'
            }
        else:
            return {
                'success': True,
                'message': 'Filterset deleted successful.'
            }

