import unittest

class test_002(unittest.TestCase):

    def setUp(self):
        self.Variable_A = "Hola Udemy"
        self.Variable_B = "Hola"


    def test_comparacion(self):

        assert self.Variable_B in self.Variable_A, f"Los valores son distintos, {self.Variable_A} != {self.Variable_B}"

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()
