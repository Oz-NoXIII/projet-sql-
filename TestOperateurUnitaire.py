import unittest
from fct_utile import Relation
from OperateurUnitaire import project, select, rename


class OpUTest(unittest.TestCase):
    """Test case utilisé pour tester les fonctions du module OperateurUnitaire"""

    def test_select(self):
        """Teste le fonctionnement de la fonction select"""

        rel = Relation('Personne', {'ID': [1, 2, 3], 'Nom': ['alice', 'bob', 'gildas']})
        attr = 'Nom'
        const = "'alice'"
        print(type(const))
        self.assertEqual(select(rel, "=", attr, const, 0).name, "SELECT * FROM Personne WHERE Nom='alice'")

    def test_project(self):
        """Teste le fonctionnement de la fonction project"""

        # résultat
        rel = Relation("rel", {'a': [1], 'b': [2]})
        self.assertEqual(type(project(rel, 'a', 'b', 'b')), Relation)
        self.assertEqual(project(rel, 'a', 'b', 'b').name, "select a, b from rel")

    def test_rename(self):
        """Teste le fonctionnement de la fonction rename"""

        rel = Relation('Personne', {'ID': [1, 2, 3], 'Nom': ['alice', 'bob', 'gildas']})
        print(f"{rename(rel, 'Nom', 'Login').name}")
        self.assertEqual(rename(rel, 'Nom', 'Login').name, "ALTER TABLE Personne RENAME COLUMN Nom TO Login")


if __name__ == '__main__':
    unittest.main()
