import unittest
import fct_utile
from OperateurUnitaire import project, select, rename


class OpUTest(unittest.TestCase):
    """Test case utilisé pour tester les fonctions du module OperateurUnitaire"""

    def test_select(self):
        """Teste le fonctionnement de la fonction select"""
        pass

    def test_project(self):
        """Teste le fonctionnement de la fonction project"""

        rel = fct_utile.Relation("rel", {'a': 1, 'b': 2})
        self.assertEqual(type(project(rel, 'a', 'b', 'b')), str)
        self.assertEqual(project(rel, 'a', 'b', 'b'), "select a, b from rel")

    def test_rename(self):
        """Teste le fonctionnement de la fonction rename"""
        pass


if __name__ == '__main__':
    unittest.main()
