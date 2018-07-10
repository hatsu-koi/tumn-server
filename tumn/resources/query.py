from flask_restful import reqparse, Resource


parser = reqparse.RequestParser()
parser.add_argument("filters", "json")
parser.add_argument("text", "json")


class Query(Resource):
    def post(self):
        args = parser.parse_args()

        return [["miszehbrgbk", [[9, 13], [19, 23]]]]
