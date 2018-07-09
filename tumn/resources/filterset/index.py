from flask_restful import reqparse, Resource
from tumn.core.filterset import FilterSet, filterset_store, message_queue_store
import shutil
import os
import queue

parser = reqparse.RequestParser()
parser.add_argument('url', location='json')
parser.add_argument('target', location='args')


class FilterSetMessage(Resource):
    def get(self):
        args = parser.parse_args()
        try:
            q = message_queue_store[args['target']]
        except KeyError:
            return {'message': ''}
        result_list = []
        while not q.empty():
            result_list.append(q.get())

        return {'message': '\n'.join(result_list)}


class FilterSetManager(Resource):
    def get(self):
        return [FilterSet.read_metadata(f) for f in FilterSet.filterset_paths()]

    def post(self):
        args = parser.parse_args()
        q = queue.Queue()
        name = os.path.basename('filterset').replace('.git', '')
        filterset = FilterSet(name)
        message_queue_store.iterload([args['url'], name], [q])

        FilterSet.download_filter(args['url'], q)
        q.put('FilterSet download complete. Loading FilterSet...')

        filterset.load()

    def delete(self, id_):
        try:
            path = filterset_store[id_].path
        except KeyError:
            return {
                'success': False,
                'message': 'Filterset not found.'
            }
        else:
            shutil.rmtree(path)
            del filterset_store[id_]

            return {
                'success': True,
                'message': ''
            }

