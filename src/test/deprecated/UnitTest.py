import unittest


class TestUnitTest(unittest.TestCase):

    def setUp(self):
        self.Variable_A = 50
        self.Variable_B = 50

    def test001(self):
        self.assertEqual(self.Variable_A, self.Variable_B, "Los valores son distintos")

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()
