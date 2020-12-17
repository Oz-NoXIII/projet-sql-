import unittest

import SQlLiteManage
import main

name = "test"
attributes = {"a": ["0", "1", "2"], "b": [0, 1, 2],
              "c": [0.0, 1.0, 2.0], "d": ["a", "b", "c"]}


class MTest(unittest.TestCase):

    def test_relation(self):
        rel = main.relation(name, attributes)
        self.assertTrue(rel.name == name)
        self.assertTrue(rel.attributes == attributes)
        a = ('0', 0, 0.0, 'a')
        b = ('1', 1, 1.0, 'b')
        c = ('2', 2, 2.0, 'c')
        for row in SQlLiteManage.execute('SELECT * FROM test'):
            self.assertTrue(row == a or b or c)
        SQlLiteManage.delete(name)

    def test_select(self):
        rel = main.relation(name, attributes)
        a = ('1', 1, 1.0, 'b')
        requete = main.select(rel, "=", "b", 1, 0)
        for row in SQlLiteManage.execute(requete.name):
            self.assertTrue(row == a)
        SQlLiteManage.delete(name)

    def test_project(self):
        rel = main.relation(name, attributes)
        requete = main.project(rel, "d", "b", "a")
        a = ('a', 0, '0')
        b = ('b', 1, '1')
        c = ('c', 2, '2')
        for row in SQlLiteManage.execute(requete.name):
            self.assertTrue(row == a or b or c)
        SQlLiteManage.delete(name)

    def test_rename(self):
        attri = {"a": ["0", "1", "2"], "b": [0, 1, 2],
                 "c": [0.0, 1.0, 2.0], "d": ["a", "b", "c"]}
        rel = main.relation(name, attri)
        old_name = "a"
        new_name = "z"
        main.rename(rel, old_name, new_name)
        a = ('0',)
        b = ('1',)
        c = ('2',)
        r = SQlLiteManage.execute(f'SELECT {new_name} FROM test')
        for row in r:
            self.assertTrue(row == a or b or c)
        SQlLiteManage.delete(name)

    def test_join(self):
        attri1 = {"A": [1, 1, 2, 2], "B": [3, 4, 4, 3], "C": [5, 5, 5, 6]}
        rel1 = main.relation("rel1", attri1)
        attri2 = {"C": [5, 5, 5, 6], "D": [2, 2, 1, 1], "B": [3, 4, 4, 4]}
        rel2 = main.relation("rel2", attri2)
        a = (1, 3, 5, 2)
        b = (1, 4, 5, 1)
        c = (1, 4, 5, 2)
        d = (2, 4, 5, 1)
        e = (2, 4, 5, 2)
        requete = main.join(rel1, rel2)
        for row in SQlLiteManage.execute(requete.name):
            self.assertTrue(row == a or b or c or d or e)
        SQlLiteManage.delete("rel1")
        SQlLiteManage.delete("rel2")

    def test_union(self):
        attri1 = {"A": [1, 1], "B": [3, 4], "C": [5, 5]}
        rel1 = main.relation("rel1", attri1)
        attri2 = {"A": [1, 2], "C": [5, 6], "B": [4, 3]}
        rel2 = main.relation("rel2", attri2)
        a = (1, 3, 5)
        b = (1, 4, 5)
        c = (2, 3, 6)
        requete = main.union(rel1, rel2)
        for row in SQlLiteManage.execute(requete.name):
            self.assertTrue(row == a or b or c)
        SQlLiteManage.delete("rel1")
        SQlLiteManage.delete("rel2")

    def test_difference(self):
        attri1 = {"A": [1, 1], "B": [3, 4], "C": [5, 5]}
        rel1 = main.relation("rel1", attri1)
        attri2 = {"A": [1, 2], "C": [5, 6], "B": [4, 3]}
        rel2 = main.relation("rel2", attri2)
        a = (1, 3, 5)
        requete = main.difference(rel1, rel2)
        for row in SQlLiteManage.execute(requete.name):
            self.assertTrue(row == a)
        SQlLiteManage.delete("rel1")
        SQlLiteManage.delete("rel2")


if __name__ == '__main__':
    unittest.main()
    SQlLiteManage.close()