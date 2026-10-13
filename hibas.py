import unittest

def hibas_abs(szam):
    return abs(szam)

class TestHibasABS(unittest.TestCase):
    def test_1_poz(self):
        self.assertGreaterEqual(hibas_abs(5), 0)
        
    def test_2_neg(self):
        self.assertGreaterEqual(hibas_abs(-5), 0)
        
    def test_3_zero(self):
        self.assertEqual(hibas_abs(0), 0)

if __name__ == '__main__':
    unittest.main()