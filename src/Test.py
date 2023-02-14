import unittest

from main_program import silabas

class TestSeparadorSilabas(unittest.TestCase):
    def test_separarSilabas(self):
        self.assertEqual(silabas("abono"), ["a","bo","no"])
        self.assertEqual(silabas("catalogo"), ["ca","ta","lo","go"])
        self.assertEqual(silabas("ordinador"), ["or","di","na","dor"])
        self.assertEqual(silabas("platja"), ["plat", "ja"])

if __name__ == "__main__":
    unittest.main()