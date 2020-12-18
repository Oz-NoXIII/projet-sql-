import unittest

import SQlLiteManage
import SPJRUDtoSQL

name = "test"
attributes = {"a": ["0", "1", "2"], "b": [0, 1, 2],
              "c": [0.0, 1.0, 2.0], "d": ["a", "b", "c"]}


class STSTest(unittest.TestCase):
    """Test case utilisé pour tester les fonctions du module SPJRUDtoSQL"""

    def test_relation(self):
        """Teste le fonctionnement de la fonction relation"""

        rel = SPJRUDtoSQL.relation(name, attributes)
        self.assertTrue(rel.name == name)
        self.assertTrue(rel.attributes == attributes)
        a = [('0', 0, 0.0, 'a'), ('1', 1, 1.0, 'b'), ('2', 2, 2.0, 'c')]
        result = SQlLiteManage.execute('SELECT * FROM test')
        self.assertTrue(result == a)

    def test_selectcst(self):
        """Teste le fonctionnement de la fonction select"""

        rel = SPJRUDtoSQL.relation(name, attributes)
        a = [('1', 1, 1.0, 'b')]
        requete = SPJRUDtoSQL.select(rel, "=", "d", "b", 0)
        result = SQlLiteManage.run(requete)
        self.assertTrue(result == a)

        # teste run
        SPJRUDtoSQL.run(requete)

        # teste create et display
        SPJRUDtoSQL.create("selection", requete)
        SPJRUDtoSQL.display("selection")

        # suppression des tables
        SQlLiteManage.delete(name)
        SQlLiteManage.delete("selection")

    def test_selectattrib(self):
        """Teste le fonctionnement de la fonction select"""

        attrib = {"A": ["z", "b", "y"], "B": [0, 1, 2],
                  "C": [0.0, 1.0, 2.0], "D": ["a", "b", "c"]}
        rel = SPJRUDtoSQL.relation(name, attrib)
        a = [('b', 1, 1.0, 'b')]
        requete = SPJRUDtoSQL.select(rel, "=", "A", "D", 1)
        result = SQlLiteManage.run(requete)
        self.assertTrue(result == a)
        SQlLiteManage.delete(name)

    def test_project(self):
        """Teste le fonctionnement de la fonction project"""

        rel = SPJRUDtoSQL.relation(name, attributes)
        a = [('a', 0, '0'), ('b', 1, '1'), ('c', 2, '2')]
        requete = SPJRUDtoSQL.project(rel, "d", "b", "a")
        result = SQlLiteManage.run(requete)
        self.assertTrue(result == a)

        # teste run
        SPJRUDtoSQL.run(requete)

        # teste create et display
        SPJRUDtoSQL.create("projection", requete)
        SPJRUDtoSQL.display("projection")

        # suppression des tables
        SQlLiteManage.delete(name)
        SQlLiteManage.delete("projection")

    def test_rename(self):
        """Teste le fonctionnement de la fonction rename"""

        rel = SPJRUDtoSQL.relation(name, attributes)
        a = [('0', 0, 0.0, 'a'), ('1', 1, 1.0, 'b'), ('2', 2, 2.0, 'c')]
        requete = SPJRUDtoSQL.rename(rel, "a", "z")
        result = SQlLiteManage.run(requete)
        self.assertTrue(result == a)

        # teste run
        SPJRUDtoSQL.run(requete)

        # teste create et display
        SPJRUDtoSQL.create("renommage", requete)
        SPJRUDtoSQL.display("renommage")

        # suppression des tables
        SQlLiteManage.delete(name)
        SQlLiteManage.delete("renommage")

    def test_join(self):
        """Teste le fonctionnement de la fonction join"""

        attri1 = {"A": [1, 1, 2, 2], "B": [3, 4, 4, 3], "C": [5, 5, 5, 6]}
        rel1 = SPJRUDtoSQL.relation("rel1", attri1)
        attri2 = {"C": [5, 5, 5, 6], "D": [2, 2, 1, 1], "B": [3, 4, 4, 4]}
        rel2 = SPJRUDtoSQL.relation("rel2", attri2)
        a = [(1, 3, 5, 2), (1, 4, 5, 1), (1, 4, 5, 2), (2, 4, 5, 1), (2, 4, 5, 2)]
        requete = SPJRUDtoSQL.join(rel1, rel2)
        result = SQlLiteManage.run(requete)
        self.assertTrue(result == a)

        # teste run
        SPJRUDtoSQL.run(requete)

        # teste create et display
        SPJRUDtoSQL.create("jointure", requete)
        SPJRUDtoSQL.display("jointure")

        # suppression des tables
        SQlLiteManage.delete("rel1")
        SQlLiteManage.delete("rel2")
        SQlLiteManage.delete("jointure")

    def test_union(self):
        """Teste le fonctionnement de la fonction union"""

        attri1 = {"A": [1, 1], "B": [3, 4], "C": [5, 5]}
        rel1 = SPJRUDtoSQL.relation("rel1", attri1)
        attri2 = {"A": [1, 2], "C": [5, 6], "B": [4, 3]}
        rel2 = SPJRUDtoSQL.relation("rel2", attri2)
        a = [(1, 3, 5), (1, 4, 5), (2, 3, 6)]
        requete = SPJRUDtoSQL.union(rel1, rel2)
        result = SQlLiteManage.run(requete)
        self.assertTrue(result == a)

        # teste run
        SPJRUDtoSQL.run(requete)

        # teste create et display
        SPJRUDtoSQL.create("uni", requete)
        SPJRUDtoSQL.display("uni")

        # suppression des tables
        SQlLiteManage.delete("rel1")
        SQlLiteManage.delete("rel2")
        SQlLiteManage.delete("uni")

    def test_difference(self):
        """Teste le fonctionnement de la fonction difference"""

        attri1 = {"A": [1, 1], "B": [3, 4], "C": [5, 5]}
        rel1 = SPJRUDtoSQL.relation("rel1", attri1)
        attri2 = {"A": [1, 2], "C": [5, 6], "B": [4, 3]}
        rel2 = SPJRUDtoSQL.relation("rel2", attri2)
        a = [(1, 3, 5)]
        requete = SPJRUDtoSQL.difference(rel1, rel2)
        result = SQlLiteManage.run(requete)
        self.assertTrue(result == a)

        # teste run
        SPJRUDtoSQL.run(requete)

        # teste create et display
        SPJRUDtoSQL.create("difference", requete)
        SPJRUDtoSQL.display("difference")

        # suppression des tables
        SQlLiteManage.delete("rel1")
        SQlLiteManage.delete("rel2")
        SQlLiteManage.delete("difference")

    def test_display(self):
        """Teste le fonctionnement de la fonction display"""
        # voir les tests ci-dessus
        pass

    def test_create(self):
        """Teste le fonctionnement de la fonction create"""
        # voir les tests ci-dessus
        pass


if __name__ == '__main__':
    unittest.main()
    SQlLiteManage.close()
