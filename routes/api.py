"""The Endpoints to query gene autocomplete"""

from flask import jsonify, abort, request, Blueprint
from controllers import searchGene

API = Blueprint('api', __name__)
db = None
cache = None

def get_blueprint(mysqlDB, appCache):
    """Return the blueprint for the main app module"""
    global db, cache
    db = mysqlDB
    cache = appCache
    return API

@API.route('/gene', methods=['GET'])
def getGene():
    controller = searchGene.SearchGeneController(db, cache)
    response = controller.handleRequest()
    return jsonify(response), 200

# @API.route('/', defaults={'path': ''})
# @API.route('/<path:path>')
# def catch_all(path):
#     abort(405)