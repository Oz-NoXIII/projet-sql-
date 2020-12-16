import unittest

from SQlLiteManage import create


class SQLMTest(unittest.TestCase):
    def test_create(self):
        name = "test"
        d = {"a": ["0", "1", "2"], "b": [0, 1, 2], "c": [0.0, 1.0, 2.0], "d": ["a", "b", "c"]}
        # print(create(name, d))
        # TODO


if __name__ == '__main__':
    unittest.main()
