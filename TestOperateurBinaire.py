import unittest
from OperateurBinaire import join, union, difference
from fct_utile import Relation, AttributesError


class OpBTest(unittest.TestCase):
    """Test case utilisé pour tester les fonctions du module OperateurUnitaire"""

    def test_join(self):
        """Teste le fonctionnement de la fonction join"""

        # erreur d'attribut sur rel1 et rel2: pas d'attribut en commun
        rel1 = Relation("rel1", {"a": [1], "b": [2]})
        rel2 = Relation("rel2", {"c": [1], "d": [2]})
        with self.assertRaises(AttributesError):
            join(rel1, rel2)

        # résultat
        rel1 = Relation("rel1", {"a": [1], "b": [2]})
        rel2 = Relation("rel2", {"b": [1], "c": [2]})
        self.assertEqual(type(join(rel1, rel2)), Relation)
        self.assertEqual(join(rel1, rel2).name, "SELECT * FROM rel1 NATURAL JOIN rel2")
        for attribute in ["a", "b", "c"]:
            if attribute == "a":
                self.assertEqual(type(join(rel1, rel2).attributes[attribute][0]), type(rel1.attributes[attribute][0]))
            elif attribute == "c":
                self.assertEqual(type(join(rel1, rel2).attributes[attribute][0]), type(rel2.attributes[attribute][0]))
            else:
                self.assertEqual(type(join(rel1, rel2).attributes[attribute][0]), type(rel1.attributes[attribute][0]))

    def test_union(self):
        """Teste le fonctionnement de la fonction union"""
        # erreur d'attribut sur rel1 et rel2: attributs différents
        rel1 = Relation("rel1", {"a": [1], "b": [2]})
        rel2 = Relation("rel2", {"c": [1], "d": [2]})
        with self.assertRaises(AttributesError):
            union(rel1, rel2)

        # résultat
        rel1 = Relation("rel1", {"a": [1], "b": [2]})
        rel2 = Relation("rel2", {"a": [1], "b": [2]})
        self.assertEqual(type(union(rel1, rel2)), Relation)
        self.assertEqual(union(rel1, rel2).name, "SELECT * FROM rel1 UNION SELECT * FROM rel2")
        for attribute in ["a", "b"]:
            self.assertEqual(type(union(rel1, rel2).attributes[attribute][0]), type(rel1.attributes[attribute][0]))

    def test_difference(self):
        """Teste le fonctionnement de la fonction différence"""

        # erreur d'attribut sur rel1 et rel2: attributs différents
        rel1 = Relation("rel1", {"a": [1], "b": [2]})
        rel2 = Relation("rel2", {"c": [1], "d": [2]})
        with self.assertRaises(AttributesError):
            difference(rel1, rel2)

        # résultat
        rel1 = Relation("rel1", {"a": [1], "b": [2]})
        rel2 = Relation("rel2", {"a": [1], "b": [2]})
        self.assertEqual(type(difference(rel1, rel2)), Relation)
        self.assertEqual(difference(rel1, rel2).name, "SELECT * FROM rel1 EXCEPT SELECT * FROM rel2")
        for attribute in ["a", "b"]:
            self.assertEqual(type(difference(rel1, rel2).attributes[attribute][0]), type(rel1.attributes[attribute][0]))


if __name__ == '__main__':
    unittest.main()
