import unittest
import SQlLiteManage
import SPJRUDtoSQL


class SQLMTest(unittest.TestCase):
    """Test case utilisé pour tester les fonctions du module SQlLiteManage"""

    def test_create(self):
        """Teste le fonctionnement de la fonction create"""

        name = "test"
        d = {"a": ["0", "1", "2"], "b": [0, 1, 2], "c": [0.0, 1.0, 2.0], "d": ["a", "b", "c"]}
        SQlLiteManage.create(name, d)
        d = SQlLiteManage.execute('SELECT * FROM test')
        self.assertTrue(d == [('0', 0, 0.0, 'a'), ('1', 1, 1.0, 'b'), ('2', 2, 2.0, 'c')])
        SQlLiteManage.delete(name)

    def test_relation_order(self):
        """Teste le fonctionnement de la fonction relation_order"""

        relation1 = SQlLiteManage.create('Personne', {'ID': [1, 2, 3], 'Nom': ['alice', 'bob', 'gildas']})
        relation2 = SQlLiteManage.create('Humain', {'Nom': ['jean', 'bob', 'francois'], 'ID': [4, 5, 6]})
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

    def test_run(self):
        """Teste le fonctionnement de la fonction de la fonction run sur les commandes
        imbriquées"""

        attri1 = {"A": [1, 1, 2, 2], "B": [3, 4, 4, 3], "C": [5, 5, 5, 6]}
        rel1 = SPJRUDtoSQL.relation("rel1", attri1)
        attri2 = {"C": [5, 5, 5, 6], "D": [2, 2, 1, 1], "B": [3, 4, 4, 4]}
        rel2 = SPJRUDtoSQL.relation("rel2", attri2)
        a = [(1,)]
        requete = SPJRUDtoSQL.project((SPJRUDtoSQL.select(SPJRUDtoSQL.join(rel1, rel2), "=", 'B', 3, 0)), 'A')
        result = SQlLiteManage.run(requete)
        self.assertTrue(result == a)
        SQlLiteManage.delete(rel1.name)
        SQlLiteManage.delete(rel2.name)


if __name__ == '__main__':
    unittest.main()
    SQlLiteManage.close()
