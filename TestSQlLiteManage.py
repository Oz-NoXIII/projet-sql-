import unittest

import SQlLiteManage
import main


class SQLMTest(unittest.TestCase):
    def test_create(self):
        name = "test"
        d = {"a": ["0", "1", "2"], "b": [0, 1, 2], "c": [0.0, 1.0, 2.0], "d": ["a", "b", "c"]}
        SQlLiteManage.create(name, d)
        a = ('0', 0, 0.0, 'a')
        b = ('1', 1, 1.0, 'b')
        c = ('2', 2, 2.0, 'c')
        for row in SQlLiteManage.execute('SELECT * FROM test'):
            self.assertTrue(row == a or b or c)
        SQlLiteManage.delete(name)

    def test_order(self):
        relation1 = main.relation('Personne', {'ID': [1, 2, 3], 'Nom': ['alice', 'bob', 'gildas']})
        relation2 = main.relation('Humain', {'Nom': ['jean', 'bob', 'francois'], 'ID': [4, 5, 6]})
        SQlLiteManage.relations_order(relation2, relation1)
        SQlLiteManage.execute(f"SELECT * FROM {relation2.name}")
        result = list(SQlLiteManage.cursor.description)
        col1 = [i[0] for i in result]
        SQlLiteManage.execute(f"SELECT * FROM {relation1.name}")
        result = list(SQlLiteManage.cursor.description)
        col2 = [i[0] for i in result]
        self.assertEqual(col1, col2)
        SQlLiteManage.delete(relation1.name)
        SQlLiteManage.delete(relation2.name)


if __name__ == '__main__':
    unittest.main()
    SQlLiteManage.close()
