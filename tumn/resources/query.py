from flask_restful import Resource


class Query(Resource):
    def get(self):
        return [['miszehbrgbk', [[9, 13], [19, 23]]]]
