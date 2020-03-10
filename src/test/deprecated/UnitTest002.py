import unittest


class TestUnitTest(unittest.TestCase):

    def setUp(self):
        self.Variable_A = 40
        self.Variable_B = 50

    def test002(self):
        self.assertNotEqual(self.Variable_A, self.Variable_B, "Los valores no son distintos")

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()
