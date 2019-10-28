import unittest
from utils import mysqlUtils

class test_mysqlUtils(unittest.TestCase):
    def setUp(self):
        pass

    ##
    def test_sqlRowToJsonDict(self):
        payload = (('ENSZALG00000011220', 'TRPV4', 'zonotrichia_albicollis'), ('ENSZALG00000005621', 'TRPV6', 'zonotrichia_albicollis'))
        res = mysqlUtils.sqlRowToJsonDict(payload, ['id', 'name', 'species'])
        exp = [{'id': 'ENSZALG00000011220', 'name': 'TRPV4', 'species': 'zonotrichia_albicollis'},
{'id': 'ENSZALG00000005621', 'name': 'TRPV6', 'species': 'zonotrichia_albicollis'}]
        self.assertEqual(res, exp);
            

    def tearDown(self):
        pass

# if __name__ == "__main__":
#     unittest.main()