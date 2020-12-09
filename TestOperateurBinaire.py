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
        self.assertEqual(join(rel1, rel2).name, "select * from rel1 natural join rel2")

    def test_union(self):
        """Teste le fonctionnement de la fonction union"""
        pass  # TODO

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
        self.assertEqual(difference(rel1, rel2).name, "select * from rel1 except select * from rel2")


if __name__ == '__main__':
    unittest.main()
