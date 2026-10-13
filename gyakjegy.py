import unittest

pont = int(input("A pontszamod: "))

def eredmeny(pont):
    if 101 > pont > 84:
        return f"A pontszamod: Jeles (5)"
    elif 85 > pont > 69:
        return f"A pontszamod: Jó (4)"
    elif 70 > pont > 54:
        return f"A pontszamod: Közepes (3)"
    elif 55 > pont > 39:
        return f"A pontszamod: Elégséges (2)"
    elif 40 > pont > -1:
        return f"A pontszamod: Elégtelen (1)"
    else:
        return f"Ervenytelen ertek!"    
    
print(eredmeny(pont))

class TestGyakjegy(unittest.TestCase):
    def test_1_5(self):
        self.assertEqual(eredmeny(85), "A pontszamod: Jeles (5)")
        
    def test_2_4(self):
        self.assertEqual(eredmeny(70), "A pontszamod: Jó (4)")
        
    def test_3_3(self):
        self.assertEqual(eredmeny(59), "A pontszamod: Közepes (3)")

    def test_4_2(self):
        self.assertEqual(eredmeny(54), "A pontszamod: Elégséges (2)")
        
    def test_5_1(self):
        self.assertEqual(eredmeny(0), "A pontszamod: Elégtelen (1)")
        
    def test_6_hibas(self):
        self.assertEqual(eredmeny(101), "Ervenytelen ertek!")

    def test_7_hibas(self):
        self.assertEqual(eredmeny(-12), "Ervenytelen ertek!")

if __name__ == '__main__':
    unittest.main()