import unittest

szam = int(input("Adj meg egy számot: "))

def negyzetgyok(szam):
    if szam < 0:
        return "Negativ szambol nem vonunk negyzetgyokot!"
    else:
        return szam ** 0.5

print(negyzetgyok(szam))
    
class TestGyoker(unittest.TestCase):
    def test_egeszszam_1(self):
        self.assertEqual(negyzetgyok(25), 5)
    
    def test_hibasszam(self):
        self.assertEqual(negyzetgyok(-23),"Negativ szambol nem vonunk negyzetgyokot!")
                   
if __name__ == '__main__':
    unittest.main()