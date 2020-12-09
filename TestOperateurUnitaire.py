import unittest
from fct_utile import Relation
from OperateurUnitaire import project, select, rename


class OpUTest(unittest.TestCase):
    """Test case utilisé pour tester les fonctions du module OperateurUnitaire"""

    def test_select(self):
        """Teste le fonctionnement de la fonction select"""
        pass  # TODO

    def test_project(self):
        """Teste le fonctionnement de la fonction project"""

        # résultat
        rel = Relation("rel", {'a': [1], 'b': [2]})
        self.assertEqual(type(project(rel, 'a', 'b', 'b')), Relation)
        self.assertEqual(project(rel, 'a', 'b', 'b').name, "select a, b from rel")

    def test_rename(self):
        """Teste le fonctionnement de la fonction rename"""
        pass  # TODO


if __name__ == '__main__':
    unittest.main()
