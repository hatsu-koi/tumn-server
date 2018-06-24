from git import Repo, RemoteProgress
from tumn.utils.database import Database
import os
import json
import queue

FILTERS_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), '../filters/'))


class FilterSet:
    __slots__ = ['name', 'path', 'meta', 'isLoaded', 'message_queue', 'filters']

    def __init__(self, name):
        self.name = name
        self.path = os.path.join(FILTERS_PATH, name)
        self.meta = None
        self.isLoaded = False
        self.filters = {}

    def load(self):
        self.meta = FilterSet.read_metadata(self.path)

        if not self.meta:
            return

        filterset_store.iterload([self.name, self.path, self.meta['id']], [self])
        message_queue_store.iterload([self.name, self.meta['information']['source']['href']], [queue.Queue()])

        for f in self.meta['options']:
            self.filters[f['id']] = Filter(id_=f['id'], name=f['name'],
                                           description=f['description'], tfsession=None)

        message_queue_store[self.name].put('Filter loaded successful.')

        self.isLoaded = True

    @classmethod
    def download_filter(cls, url, q):
        name = os.path.basename(url).replace('.git', '')

        class Progress(RemoteProgress):
            def update(self, op_code, cur_count, max_count=None, message=''):
                q.put(self._cur_line)

        q.put('Downloading Filterset...')
        q.put('FilterSet detected : {}'.format(name))

        return Repo.clone_from(url,
                               os.path.join('tumn/filters', name),
                               progress=Progress())

    @classmethod
    def read_metadata(cls, path):
        try:
            with open(os.path.join(path, 'filter.json')) as f:
                return json.load(f)
        except FileNotFoundError:
            print('filter.json not found in {}'.format(path))

    @classmethod
    def load_filters(cls):
        for filterset_path in FilterSet.filterset_paths():
            f = cls(os.path.basename(filterset_path))
            f.load()

    @classmethod
    def filterset_paths(cls):
        return [os.path.join(os.path.abspath(os.path.join(os.path.dirname(__file__), '../filters/')), d)
                for d in os.listdir(FILTERS_PATH) if os.path.isdir(os.path.join(FILTERS_PATH, d))]


class Filter:
    __slots__ = ['id', 'name', 'description', 'tfsession']

    def __init__(self, id_, name, description, tfsession):
        self.id = id_
        self.name = name
        self.description = description
        self.tfsession = tfsession

    def predict(self, *args, **kwargs):
        pass


filterset_store = Database()
message_queue_store = Database()
