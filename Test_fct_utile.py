import unittest
from fct_utile import Relation, argsinrel, removeduplicate, ErrorKey, havesametype, ErrorType, arelists, len_is_cst, \
    isarelation


class FctUTest(unittest.TestCase):
    """Test case utilisé pour tester les fonctions et classe du module fct_utile

    Affiche normalement ces avertissements dans la console:

    La clé b ne pointe pas vers une liste.

    Il y a au moins deux types différents dans la liste dont <class 'int'> et <class 'str'>.

    Format Incompatible: <class 'int'> différent de <class 'str'>

    Format Incompatible: <class 'int'> différent de <class 'float'>

    Les tailles des listes ne sont pas constantes.

    Format Incompatible: <class 'int'> différent de <class 'str'>

    La clé a pointe vers une liste vide.

    Les tailles des listes ne sont pas constantes."""

    def test_havesametype(self):
        """Teste le fonctionnement de la fonction havesametype"""
        args = "a"
        with self.assertRaises(ErrorType):
            havesametype(args)
        args = ["a", 1, "b"]
        self.assertFalse(havesametype(args))
        args = ["a", 1]
        self.assertFalse(havesametype(args))
        args = [1.0, 1]
        self.assertFalse(havesametype(args))
        args = ["a", "b"]
        self.assertTrue(havesametype(args))

    def test_arelists(self):
        """Teste le fonctionnement de la fonction arelists"""
        dico = "a"
        with self.assertRaises(ErrorType):
            arelists(dico)
        dico = {"a": [], "b": 2}
        self.assertFalse(arelists(dico))
        dico = {"a": [], "b": []}
        self.assertTrue(arelists(dico))

    def test_len_is_cst(self):
        """Teste le fonctionnement de la fonction len_is_cst"""

        dico = "a"
        with self.assertRaises(ErrorType):
            arelists(dico)
        dico = {"a": [], "b": []}
        self.assertFalse(len_is_cst(dico))
        dico = {"a": [1], "b": []}
        self.assertFalse(len_is_cst(dico))
        dico = {"a": [1], "b": [2]}
        self.assertTrue(len_is_cst(dico))

    def test_isarelation(self):
        """Teste le fonctionnement de la fonction isarelation"""

        dico = "a"
        with self.assertRaises(ErrorType):
            arelists(dico)
        dico = {"a": ["a"], "b": ["b", "c"]}
        self.assertFalse(len_is_cst(dico))
        self.assertTrue((havesametype(dico["b"])))
        self.assertTrue(havesametype(dico["a"]))
        dico = {"a": ["a", 1], "b": ["b", "c"]}
        self.assertTrue(len_is_cst(dico))
        self.assertTrue((havesametype(dico["b"])))
        self.assertFalse(havesametype(dico["a"]))
        dico = {"a": [1, 2], "b": [1.1, 2.2]}
        self.assertTrue(len_is_cst(dico))
        self.assertTrue((havesametype(dico["a"])))
        self.assertTrue((havesametype(dico["b"])))

    def test_removeduplicate(self):
        """Teste le fonctionnement de la fonction removeduplicate"""

        args = "a"
        with self.assertRaises(ErrorType):
            removeduplicate(args)
        args = ["a"]
        self.assertTrue(args == removeduplicate(args))
        self.assertTrue(len(args) >= len(removeduplicate(args)))
        args = ["a", "a"]
        self.assertFalse(args == removeduplicate(args))
        self.assertTrue(len(args) >= len(removeduplicate(args)))

    def test_argsinrel(self):
        """Teste le fonctionnement de la fonction argsinrel"""

        rel = {}
        args = "a"
        with self.assertRaises(ErrorType):
            argsinrel(rel, args)
        rel = Relation("rel", {"a": [1], "b": [2]})
        args = ["a"]
        self.assertTrue(argsinrel(rel, args))


if __name__ == '__main__':
    unittest.main()
