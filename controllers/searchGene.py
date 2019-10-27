from flask import request, abort
from constants import keyLabels
from utils import mysqlUtils

class SearchGeneController:  # TODO: consider parent class Controller
    """Get gene autocomplete data by name prefix and species if available
    @param name: the name prefix, case incensitive, length must be at least 3
    @param species: the species name (optional)
    @return: 200: a list of json objects each with keys "id", "name" & "species"
    @raise 405: if params are invalid
    """
    def __init__(self, db, cache):
        self.db = db
        self.cache = cache

    def handleRequest(self, parequestrams=request):
        geneName, geneSpecies = self._validateParams()

        query, args = self._contructQuery(geneName, geneSpecies)
        rows = mysqlUtils.executeQuery(self.db, query, args)
        jsonDict = mysqlUtils.sqlRowToJsonDict(rows, rowHeaders=['id', 'name', 'species'])
        return jsonDict

    def _queryCache(self, geneName, geneSpecies):
        # TODO: Design sharded trie cache. Assuming the design would be a write through cache
        return None  

    def _contructQuery(self, geneName, geneSpecies):
        query = "SELECT stable_id, display_label, species from gene_autocomplete WHERE display_label LIKE %s"
        args = [geneName + "%%"]
        if geneSpecies != None:
            query += ' AND species=%s'
            args.append(geneSpecies)
        return (query, args)

    def _validateParams(self, request=request):
        geneName = request.args.get(keyLabels.name)
        geneSpecies = request.args.get(keyLabels.species)
        if geneName == None:
            abort(400)
        if len(geneName) < 3: # TODO: Decide where to place hardcoded 3 as a constant
            abort(400)
        return (geneName, geneSpecies)
