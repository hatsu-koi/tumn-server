from git import Repo, RemoteProgress
from tumn.utils.database import Database
import os
import json
import shutil

FILTERS_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), '../filters/'))


class FilterSet:
    __slots__ = ['name', 'path', 'meta', 'isLoaded', 'message_queue', 'filters']
    filterset_store = Database()
    message_queue = []

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

        FilterSet.filterset_store.iterload([self.name, self.path, self.meta['id']], [self])

        loaded_filter = __import__(os.path.join(self.path, self.meta['entry']))
        loaded_filter.load()

        for f in self.meta['options']:
            self.filters[f['id']] = Filter(id_=f['id'],
                                           name=f['name'],
                                           description=f['description'],
                                           predict=loaded_filter.filters[f['id']])

        FilterSet.message_queue.append('Filter loaded successful.')

        self.isLoaded = True

    @classmethod
    def download_filter(cls, url):
        name = os.path.basename(url).replace('.git', '')

        class Progress(RemoteProgress):
            def update(self, op_code, cur_count, max_count=None, message=''):
                cls.message_queue.append(self._cur_line)

        cls.message_queue.append('Downloading Filterset...\n'
                                 'FilterSet detected : {}'.format(name))

        return Repo.clone_from(url,
                               os.path.join('tumn/filters', name),
                               progress=Progress())

    @classmethod
    def read_metadata(cls, path):
        try:
            with open(os.path.join(path, 'filterset.json')) as f:
                return json.load(f)
        except FileNotFoundError:
            print('filterset.json not found in {}'.format(path))

    @classmethod
    def load_filters(cls):
        for filterset_path in FilterSet.filterset_paths():
            f = cls(os.path.basename(filterset_path))
            f.load()

    @classmethod
    def filterset_paths(cls):
        return [os.path.join(os.path.abspath(os.path.join(os.path.dirname(__file__), '../filters/')), d)
                for d in os.listdir(FILTERS_PATH) if os.path.isdir(os.path.join(FILTERS_PATH, d))]

    @classmethod
    def find_filterset(cls, arg):
        try:
            return cls.filterset_store[arg]
        except KeyError:
            return None

    @classmethod
    def delete_filterset(cls, id_):
        path = FilterSet.find_filterset(id_).path
        shutil.rmtree(path)
        del cls.filterset_store[id_]

    @classmethod
    def pop_messages(cls):
        copy = cls.message_queue.copy()
        cls.message_queue.clear()
        return '\n'.join(copy)

    @classmethod
    def push_message(cls, message):
        cls.message_queue.append(message)


class Filter:
    __slots__ = ['id', 'name', 'description', 'predict']

    def __init__(self, id_, name, description, predict):
        self.id = id_
        self.name = name
        self.description = description
        self.predict = predict
