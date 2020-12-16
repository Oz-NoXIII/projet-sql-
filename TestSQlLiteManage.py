import unittest

from SQlLiteManage import create, relations_order
from fct_utile import Relation

class SQLMTest(unittest.TestCase):
    def test_create(self):
        name = "test"
        d = {"a": ["0", "1", "2"], "b": [0, 1, 2], "c": [0.0, 1.0, 2.0], "d": ["a", "b", "c"]}
        print(create(name, d))
        # TODO


    def test_order(self):
        relation1 = Relation('Personne', {'ID': [1, 2, 3], 'Nom': ['alice', 'bob', 'gildas']})
        relation2 = Relation('Humain', {'Nom': ['jean', 'bob', 'francois'], 'ID': [4, 5, 6]})
        create(relation1.name, relation1.attributes)

        relations_order(relation2, relation1)


if __name__ == '__main__':
    unittest.main()
