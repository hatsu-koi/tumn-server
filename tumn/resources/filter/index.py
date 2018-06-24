from flask_restful import reqparse, Resource
from tumn.core.filterset import FilterSet, filterset_store, message_queue_store
import shutil
import os
import queue

parser = reqparse.RequestParser()
parser.add_argument('filter', location='json')
parser.add_argument('target', location='args')


class FilterAPI(Resource):
    def get(self):
        args = parser.parse_args()
        if args['target']:
            try:
                q = message_queue_store[args['target']]
            except KeyError:
                return {'message': ''}
            result_list = []
            while not q.empty():
                result_list.append(q.get())

            return {'message': '\n'.join(result_list)}
        else:
            return [FilterSet.read_metadata(f) for f in FilterSet.filterset_paths()]

    def post(self):
        args = parser.parse_args()
        q = queue.Queue()
        name = os.path.basename('filter').replace('.git', '')
        filterset = FilterSet(name)
        message_queue_store.iterload([args['filter'], name], [q])

        FilterSet.download_filter(args['filter'], q)
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

