import unittest


class TestUnitTest(unittest.TestCase):

    def setUp(self):
        self.Variable_A = "Bienvenido a la clase de unittest"
        self.Variable_B = "unittest"


    def test002(self):
        self.assertIn(self.Variable_B, self.Variable_A, f"No coinciden")

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()
