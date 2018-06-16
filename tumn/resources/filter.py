from flask import make_response
from flask_restful import reqparse, Resource
from git import Repo, RemoteProgress
from os import path, listdir
import json

parser = reqparse.RequestParser()
parser.add_argument('filter',
                    dest='filter',
                    type=str,
                    location='form')

installing_message = ''


class Filter(Resource):
    def get(self):
        result = []
        filters_path = path.abspath(path.join(path.dirname(__file__), '../filters/'))
        filters = [d for d in listdir(filters_path) if path.isdir(path.join(filters_path, d))]

        for filter_path in filters:
            with open(path.join(filters_path, filter_path, 'filter.json')) as f:
                result.append(json.load(f))

        return result

    def post(self):
        global installing_message
        args = parser.parse_args()

        installing_message += 'Downloading Filter...\n'

        repo = self.download_filter(args['filter'])
        installing_message += 'Filter download complete. Installing Filter...\n'

        self.install_filter(repo.git.rev_parse("--show-toplevel"))
        installing_message += 'Filter completely installed.\n'

    def download_filter(self, url):
        global installing_message

        class Progress(RemoteProgress):
            def update(self, op_code, cur_count, max_count=None, message=''):
                global installing_message
                installing_message += self._cur_line + '\n'

        filter_name = path.basename(url).replace('.git', '')
        installing_message += 'Filter detected : {}\n'.format(filter_name)
        return Repo.clone_from(url,
                               'tumn/filters/{}'.format(filter_name),
                               progress=Progress())

    def install_filter(self, path):
        pass


class FilterInstallingStatus(Resource):
    def get(self):
        global installing_message
        message = installing_message
        installing_message = ''
        return {'message': message}


class FilterControl(Resource):
    def delete(self, id):
        self.delete_filter(id)

    def delete_filter(self, id):
        pass
