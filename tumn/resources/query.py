from flask_restful import Resource


class Query(Resource):
    def get(self):
        return [[0, 12], [16, 20]]
