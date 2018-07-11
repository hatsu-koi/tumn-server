from flask_restful import reqparse, Resource, fields, marshal_with


parser = reqparse.RequestParser()
parser.add_argument("filters", "json")
parser.add_argument("text", "json")


class Query(Resource):
    def post(self):
        args = parser.parse_args()

        return {
            "filter": "miszehbrgbk",
            "index": [[9, 13], [19, 23]]
        }
