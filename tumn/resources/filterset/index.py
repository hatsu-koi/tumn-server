from flask_restful import reqparse, Resource, fields, marshal_with
from tumn.core.filterset import FilterSet
import os

parser = reqparse.RequestParser()
parser.add_argument("url", location="json")
parser.add_argument("target", location="args")

get_filters_field = {
    "filters": fields.List(fields.Nested({
        "title": fields.String,
        "id": fields.String,
        "information": fields.Nested({
            "author": fields.String,
            "description": fields.String,
            "source": fields.Nested({
                "href": fields.String,
                "text": fields.String
            })
        }),
        "options": fields.List(fields.Nested({
            "name": fields.String,
            "id": fields.String,
            "description": fields.String
        })),
        "type": fields.String,
        "version": fields.String,
        "entry": fields.String
    })),
    "messages": fields.List(fields.String)
}

download_filterset_field = {
    "success": fields.Boolean,
    "error": fields.String
}

delete_filterset_field = {
    "success": fields.Boolean,
    "message": fields.String
}


class FilterSetManager(Resource):
    @marshal_with(get_filters_field)
    def get(self):
        return {
            "filters": [FilterSet.read_metadata(f) for f in FilterSet.filterset_paths()],
            "messages": FilterSet.pop_messages()
        }

    @marshal_with(download_filterset_field)
    def post(self):
        args = parser.parse_args()

        try:
            name = os.path.basename(args["url"]).replace(".git", "")
            filterset = FilterSet(name)

            FilterSet.download_filter(args["url"])
            FilterSet.push_message("FilterSet download complete. Loading FilterSet...")

            filterset.setup()
            filterset.load()
        except Exception as e:
            return {
                "success": False,
                "error": str(e)
            }
        else:
            return {
                "success": True,
                "error": None
            }

    @marshal_with(delete_filterset_field)
    def delete(self, id_):
        try:
            FilterSet.delete_filterset(id_)
        except (KeyError, AttributeError):
            return {
                "success": False,
                "message": "Filterset not found."
            }
        except PermissionError:
            return {
                "success": False,
                "message": "Permission denied."
            }
        else:
            return {
                "success": True,
                "message": "Filterset deleted successful."
            }
