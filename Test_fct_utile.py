import unittest
from fct_utile import Relation, argsinrel, removeduplicate, havesametype, ErrorType, arelists, len_is_cst, \
    isarginrel, joinable, isarelation, havesameattributes, listofkey, nameandtype, linedata, data


class FctUTest(unittest.TestCase):
    """Test case utilisé pour tester les fonctions et classe du module fct_utile

    Affiche des messages d'erreurs controlées dans la console

    """

    def test_argsinrel(self):
        """Teste le fonctionnement de la fonction argsinrel"""

        # erreur de type sur rel et args
        rel = {}
        args = "a"
        with self.assertRaises(ErrorType):
            argsinrel(rel, args)

        # erreur de type sur args
        rel = Relation("rel", {"a": [1], "b": [2]})
        with self.assertRaises(ErrorType):
            argsinrel(rel, args)

        # erreur de type sur rel
        rel = {}
        args = ["a"]
        with self.assertRaises(ErrorType):
            argsinrel(rel, args)

        # affichera à la console:
        # L'argument c n'appartient pas à la relation rel.
        rel = Relation("rel", {"a": [1], "b": [2]})
        args = ["c"]
        print("\ntest_argsinrel")
        self.assertFalse(argsinrel(rel, args))

        # résultat
        rel = Relation("rel", {"a": [1], "b": [2]})
        args = ["a"]
        self.assertTrue(argsinrel(rel, args))

    def test_removeduplicate(self):
        """Teste le fonctionnement de la fonction removeduplicate"""

        # erreur de type sur args
        args = "a"
        with self.assertRaises(ErrorType):
            removeduplicate(args)

        # fonctionnement sur un tuple sans doublons
        targs1 = ("a", "b", "c")
        args1 = ["a", "b", "c"]
        self.assertEqual(args1, removeduplicate(targs1))
        self.assertTrue(len(args1) >= len(removeduplicate(targs1)))

        # fonctionnement sur un tuple avec doublons
        targs2 = ("a", "a", "b", "b", "c", "c")
        args2 = ["a", "a", "b", "b", "c", "c"]
        self.assertNotEqual(args2, removeduplicate(targs2))
        self.assertTrue(len(args2) >= len(removeduplicate(targs2)))

        # résultat
        self.assertEqual(args1, removeduplicate(targs2))

    def test_isarelation(self):
        """Teste le fonctionnement de la fonction isarelation"""

        # erreur de type sur attributes
        attributes = "a"
        with self.assertRaises(ErrorType):
            isarelation(attributes)

        # erreur de type dans attributes
        attributes = {1: ["a"], "b": ["b"]}
        with self.assertRaises(ErrorType):
            isarelation(attributes)

        # résultat
        attributes = {"a": ["a"], "b": ["b"]}
        self.assertTrue((isarelation(attributes)))

    def test_len_is_cst(self):
        """Teste le fonctionnement de la fonction len_is_cst"""

        # erreur de type sur attributes
        attributes = "a"
        with self.assertRaises(ErrorType):
            arelists(attributes)

        # affichera à la console:
        # L'attribut a pointe vers une liste vide.
        attributes = {"a": [], "b": []}
        print("\ntest_len_is_cst")
        self.assertFalse(len_is_cst(attributes))

        # affichera à la console:
        # Les tailles des listes ne sont pas constantes.
        attributes = {"a": [1], "b": []}
        print("\ntest_len_is_cst")
        self.assertFalse(len_is_cst(attributes))

        # résultat
        attributes = {"a": [1], "b": [2]}
        self.assertTrue(len_is_cst(attributes))

    def test_arelists(self):
        """Teste le fonctionnement de la fonction arelists"""

        # erreur de type sur attributes
        attributes = "a"
        with self.assertRaises(ErrorType):
            arelists(attributes)

        # affichera à la console:
        # L'attribut b ne pointe pas vers une liste.
        attributes = {"a": 1, "b": 2}
        print("\ntest_arelists")
        self.assertFalse(arelists(attributes))

        # affichera à la console:
        # L'attribut b ne pointe pas vers une liste.
        attributes = {"a": [], "b": 2}
        print("\ntest_arelists")
        self.assertFalse(arelists(attributes))

        # résultat
        attributes = {"a": [], "b": []}
        self.assertTrue(arelists(attributes))

    def test_havesametype(self):
        """Teste le fonctionnement de la fonction havesametype"""

        # erreur de type sur args
        args = "a"
        with self.assertRaises(ErrorType):
            havesametype(args)

        # affichera à la console:
        # Il y a au moins deux types différents dans la liste dont <class 'int'> et <class 'str'>.
        args = ["a", 1, "b"]
        print("\ntest_havesametype")
        self.assertFalse(havesametype(args))

        # affichera à la console:
        # Format Incompatible: <class 'int'> différent de <class 'str'>
        args = ["a", 1]
        print("\ntest_havesametype")
        self.assertFalse(havesametype(args))

        # affichera à la console:
        # Format Incompatible: <class 'int'> différent de <class 'float'>
        args = [1.0, 1]
        print("\ntest_havesametype")
        self.assertFalse(havesametype(args))

        # résultat
        args = ["a", "b"]
        self.assertTrue(havesametype(args))

    def test_isarginrel(self):
        """Teste le fonctionnement de la fonction isarginrel"""

        # erreur de type sur rel
        rel = "rel"
        arg = "a"
        with self.assertRaises(ErrorType):
            isarginrel(arg, rel)

        # arg n'est pas un attribut de rel
        rel = Relation("rel", {"b": [1, 2]})
        self.assertFalse(isarginrel(arg, rel))

        # arg est une valeur dans un attribut de rel
        rel = Relation("rel", {"c": ["a", "b"]})
        self.assertFalse(isarginrel(arg, rel))

        # résultat
        rel = Relation("rel", {"a": [1, 2]})
        self.assertTrue(isarginrel(arg, rel))

    def test_joinable(self):
        """Teste le fonctionnement de la fonction joinable"""

        # erreur de type sur rel1 et rel2
        rel1 = "1"
        rel2 = "2"
        with self.assertRaises(ErrorType):
            joinable(rel1, rel2)

        # pas d'attribut en commun
        rel1 = Relation("rel1", {"a": [1], "b": [2]})
        rel2 = Relation("rel2", {"c": [1], "d": [2]})
        self.assertFalse(joinable(rel1, rel2))

        # résultat
        rel1 = Relation("rel1", {"a": [1], "b": [2]})
        rel2 = Relation("rel2", {"b": [1], "c": [2]})
        self.assertTrue(joinable(rel1, rel2))

    def test_havesameattributes(self):
        """Teste le fonctionnement de la fonction havesameattributes"""

        rel1 = "1"
        rel2 = "2"
        with self.assertRaises(ErrorType):
            havesameattributes(rel1, rel2)

        # nombres d'attributs différents
        rel1 = Relation("rel1", {"a": [1], "b": [2], "c": [3]})
        rel2 = Relation("rel2", {"a": [1], "b": [2]})
        self.assertFalse(havesameattributes(rel1, rel2))

        # attribut différent
        rel1 = Relation("rel1", {"a": [1], "b": [2]})
        rel2 = Relation("rel2", {"a": [1], "c": [2]})
        self.assertFalse(havesameattributes(rel1, rel2))

        # type différent de valeur dans un attribut de même nom
        # affichera à la console:
        # Format Incompatible: <class 'str'> différent de <class 'int'>
        rel1 = Relation("rel1", {"a": [1], "b": [2]})
        rel2 = Relation("rel2", {"a": ["a"], "b": [2]})
        print("\ntest_havesameattributes")
        self.assertFalse(havesameattributes(rel1, rel2))

        # résultat
        rel1 = Relation("rel1", {"a": [1], "b": [2]})
        rel2 = Relation("rel2", {"a": [1], "b": [2]})
        self.assertTrue(havesameattributes(rel1, rel2))

    def test_listofkey(self):
        """Teste le fonctionnement de la fonction listofkey"""

        # résultat
        d = {"a": 1, "b": 2, "c": 3}
        l = listofkey(d)
        for key in d:
            self.assertTrue(key in l)

    def test_nameandtype(self):
        """Teste le fonctionnement de la fonction nameandtype"""

        # résultat
        d = {"a": [], "b": [1], "c": [1.0], "d": ["d"]}
        l = ["a", "b", "c", "d"]
        self.assertEqual(nameandtype(d, l), "a null, b integer, c real, d text")

    def test_linedata(self):
        """Teste le fonctionnement de la fonction linedata"""

        # résultat
        d = {"a": ["0", "1"], "b": [0, 1], "c": [0.0, 1.0], "d": ["a", "b"]}
        l = ["a", "b", "c", "d"]
        self.assertEqual(linedata(d, l, 0), ('0', 0, 0.0, 'a'))
        self.assertEqual(linedata(d, l, 1), ('1', 1, 1.0, 'b'))

    def test_data(self):
        """Teste le fonctionnement de la fonction data"""

        # résultat
        d = {"a": ["0", "1", "2"], "b": [0, 1, 2], "c": [0.0, 1.0, 2.0], "d": ["a", "b", "c"]}
        l = ["a", "b", "c", "d"]
        self.assertEqual(data(d, l), [('0', 0, 0.0, 'a'), ('1', 1, 1.0, 'b'), ('2', 2, 2.0, 'c')])


if __name__ == '__main__':
    unittest.main()
