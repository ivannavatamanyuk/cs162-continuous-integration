from sqlalchemy import create_engine
import unittest
class IntegrationTest(unittest.TestCase):
    def test_postcorrect(self):
        r = requests.post('http://localhost:5000/add', data={'expression':'100+'})
        self.assertEqual(r.status_code,400)
    def test_postcorrect(self):
        r = requests.post('http://localhost:5000/add', data={'expression':'100+100'})
        self.assertEqual(r.status_code,200)
    def testdb_correct(self):
        r = requests.post('http://localhost:5000/add', data={'expression':'100+100'})
        engine = create_engine('postgresql://cs162_user:cs162_password@localhost:5432/cs162', echo =  True)
        with engine.connect() as con:
            rs = con.execute("SELECT * FROM Expression WHERE text = '100+100'")
            rows = rs.fetchall()
        self.assertEqual(len(rows), 1)
    def testdb_wrong(self):
        r = requests.post('http://localhost:5000/add', data={'expression':'100+'})
        engine = create_engine('postgresql://cs162_user:cs162_password@localhost:5432/cs162', echo =  True)
        with engine.connect() as con:
            rs = con.execute("SELECT * FROM Expression WHERE text = '100+'")
            rows = rs.fetchall()
        self.assertEqual(len(rows), 0)
