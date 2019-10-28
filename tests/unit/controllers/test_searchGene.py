import unittest, flask, mock
from mock import patch, Mock, MagicMock
from controllers import searchGene
from werkzeug.exceptions import HTTPException

class test_searchGene(unittest.TestCase):
    def setUp(self):
        self.db = Mock()
        self.db.connection.cursor.return_value.execute.return_value = None
        self.db.connection.cursor.return_value.fetchall.return_value = None

        self.cache = None
        self.controller = searchGene.SearchGeneController(self.db, self.cache)
        self.req = mock.MagicMock()

    ##
    def test_queryCache(self):
        res = self.controller._queryCache("gene", "species")
        exp = None
        self.assertEqual(res, exp);

    ##
    def test__constructQuery_all_param(self):
        res = self.controller._constructQuery("gene", "species")
        exp = ("SELECT stable_id, display_label, species from gene_autocomplete WHERE display_label LIKE %s AND species=%s", ["gene%%", "species"])
        self.assertEqual(res, exp)

    ##
    def test__constructQuery_only_name(self):
        res = self.controller._constructQuery("gene")
        exp = ("SELECT stable_id, display_label, species from gene_autocomplete WHERE display_label LIKE %s", ["gene%%"])
        self.assertEqual(res, exp)

    ##
    def test__validateParams_all_params_success(self):
        self.req.args = { "name": "gene", "species": "species" }
        res = self.controller._validateParams(self.req)
        self.assertEqual(res, ('gene', "species"))
    
    def test__validateParams_only_name_success(self):
        self.req.args = { "name": "gene" }
        res = self.controller._validateParams(self.req)
        self.assertEqual(res, ('gene', None))

    def test__validateParams_all_params_failure(self):
        with self.assertRaises(HTTPException) as http_error:
            self.req.args = { "name": "ge", "species": "species" }
            res = self.controller._validateParams(self.req)
            self.assertEqual(http_error.exception.code, 400)

    def test__validateParams_name_empty_failure(self):
        with self.assertRaises(HTTPException) as http_error:
            self.req.args = { "name": "", "species": "species" }
            res = self.controller._validateParams(self.req)
            self.assertEqual(http_error.exception.code, 400)

    
    ##
    def test_handleRequest_success(self):
        self.req.args = {"name": "gene", "species": "species"}
        self.db.cursor.return_value.fetchall.return_value = (('ENSZALG00000011220', 'TRPV4', 'zonotrichia_albicollis'), ('ENSZALG00000005621', 'TRPV6', 'zonotrichia_albicollis'))

        res = self.controller.handleRequest(self.req)
        exp = [{'id': 'ENSZALG00000011220', 'name': 'TRPV4', 'species': 'zonotrichia_albicollis'},
{'id': 'ENSZALG00000005621', 'name': 'TRPV6', 'species': 'zonotrichia_albicollis'}]
        self.assertEqual(res, exp)

    ##
    def test___init_success(self):
        res = searchGene.SearchGeneController("howdy", "partner")
        self.assertEqual(res.db, "howdy")
        self.assertEqual(res.cache, "partner")
        
            

    def tearDown(self):
        pass

# if __name__ == "__main__":
#     unittest.main()