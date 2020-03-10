import unittest


class TestUnitTest(unittest.TestCase):

    def setUp(self):
        self.Variable_A = "Mervin Alberto"


    def test002(self):
        self.assertTrue("Mervin Alberto" == self.Variable_A, "Los valores son distintos")

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()
