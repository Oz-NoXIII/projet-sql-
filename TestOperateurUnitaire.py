import unittest
from fct_utile import Relation, ComparatorError, AttributesError, ErrorType
from OperateurUnitaire import project, select, rename


class OpUTest(unittest.TestCase):
    """Test case utilisé pour tester les fonctions du module OperateurUnitaire"""

    def test_select(self):
        """Teste le fonctionnement de la fonction select"""

        # erreur de comparateur: cmp ne fait pas partie de la liste des comparators
        rel = Relation('Personne', {'ID': [1, 2, 3], 'Nom': ['alice', 'bob', 'gildas']})
        attr = 'Nom'
        const = 'alice'
        cmp = '*'
        with self.assertRaises(ComparatorError):
            select(rel, cmp, attr, const, 0)

        # erreur d'attribut: attr ne fait pas partie de rel
        cmp = '='
        attr = 'alice'
        with self.assertRaises(AttributesError):
            select(rel, cmp, attr, const, 0)

        # erreur d'attribut: const ne fait pas partie de rel
        attr = 'Nom'
        with self.assertRaises(AttributesError):
            select(rel, cmp, attr, const, 1)

        # erreur de type: argument const incompatible avec argument de attr
        const = 1
        with self.assertRaises(ErrorType):
            select(rel, cmp, attr, const, 0)

        # résultat
        const = 'alice'
        self.assertEqual(select(rel, cmp, attr, const, 0).name, "SELECT * FROM Personne WHERE Nom=alice")
        for attribute in rel.attributes:
            self.assertEqual(type(select(rel, cmp, attr, const, 0).attributes[attribute][0]),
                             type(rel.attributes[attribute][0]))
        rel = Relation('Bénéfice', {'Prix de vente': [10, 20, 30], "Prix d'achat": [30, 20, 10]})
        attr = 'Prix de vente'
        const = "Prix d'achat"
        self.assertEqual(select(rel, cmp, attr, const, 1).name, "SELECT * FROM Bénéfice "
                                                                "WHERE Prix de vente=Prix d'achat")
        for attribute in rel.attributes:
            self.assertEqual(type(select(rel, cmp, attr, const, 1).attributes[attribute][0]),
                             type(rel.attributes[attribute][0]))

    def test_project(self):
        """Teste le fonctionnement de la fonction project"""

        # résultat
        rel = Relation("rel", {'a': [1], 'b': [2]})
        self.assertEqual(type(project(rel, 'a', 'b', 'b')), Relation)
        self.assertEqual(project(rel, 'a', 'b', 'b').name, "SELECT a, b FROM rel")
        for attribute in ["a", "b"]:
            self.assertEqual(type(project(rel, 'a', 'b', 'b').attributes[attribute][0]),
                             type(rel.attributes[attribute][0]))

    def test_rename(self):
        """Teste le fonctionnement de la fonction rename"""

        # erreur d'attribut: old_name ne fait pas partie de rel
        rel = Relation('Personne', {'ID': [1, 2, 3], 'Nom': ['alice', 'bob', 'gildas']})
        old_name = 'alice'
        new_name = 'Login'
        with self.assertRaises(AttributesError):
            rename(rel, old_name, new_name)

        # résultat
        old_name = 'Nom'
        self.assertEqual(rename(rel, old_name, new_name).name, "ALTER TABLE Personne RENAME COLUMN Nom TO Login")
        self.assertFalse(old_name in rel.attributes)
        self.assertTrue(new_name in rel.attributes)


if __name__ == '__main__':
    unittest.main()
