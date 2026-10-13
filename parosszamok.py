import unittest

szam1 = int(input("Az intervallum also vegpontja: "))
szam2 = int(input("Az intervallum felso vegpontja: "))

def parosszam(szam1, szam2):
    szamossz = 0
    if szam1 % 2 != 0:
        szam1 += 1
        for i in range(szam1, szam2, 2):
            szamossz += i
    else:
        for i in range(szam1, szam2, 2):
            szamossz += i
    
    return szamossz
        
print(f"A(z) [{szam1}; {szam2}] intervallumba eso paros szamok osszege: {parosszam(szam1, szam2)}")

class ParosszamTest(unittest.TestCase):
    def test_rendes(self):
        self.assertEqual(parosszam(0,10), 20)
    
    
if __name__ == '__main__':
    unittest.main()