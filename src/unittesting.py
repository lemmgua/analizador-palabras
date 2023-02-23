import unittest

from main_program import silabas

class TestSeparadorSilabas(unittest.TestCase):
    def test_separarSilabas(self):
        self.assertEqual(silabas("abono"), ["a","bo","no"])
        self.assertEqual(silabas("cuina"), ["cui","na"])
        self.assertEqual(silabas("catálogo"), ["ca","tá","lo","go"])
        self.assertEqual(silabas("ordinador"), ["or","di","na","dor"])
        self.assertEqual(silabas("menjador"), ["men","ja","dor"])
        self.assertEqual(silabas("comptador"), ["comp","ta","dor"])
        self.assertEqual(silabas("separador"), ["se","pa","ra","dor"])
        self.assertEqual(silabas("català"), ["ca","ta","là"])
        self.assertEqual(silabas("avantguarda"), ["a","vant","guar","da"])
        #self.assertEqual(silabas("enginyería"), ["en","gi","nye","rí","a"])
    
    def test_separarAcentos(self):
        self.assertEqual(silabas("aurèola"), ["au","rè","o","la"])
        self.assertEqual(silabas("cautxú"), ["caut","xú"])
        self.assertEqual(silabas("etíop"), ["e","tí","op"])
        self.assertEqual(silabas("diòptria"), ["di","òp","tri","a"])
        self.assertEqual(silabas("esdrúixola"), ["es","drúi","xo","la"])

    def test_separarConsonanteVocal(self):
        self.assertEqual(silabas("casa"), ["ca","sa"])
        self.assertEqual(silabas("roca"), ["ro","ca"])
        self.assertEqual(silabas("pàgina"), ["pà","gi","na"])
        self.assertEqual(silabas("patata"), ["pa","ta","ta"])
        self.assertEqual(silabas("obra"), ["o","bra"])

    def test_separarConsonanteConsonanteVocal(self):
        self.assertEqual(silabas("menjador"), ["men","ja","dor"])
        self.assertEqual(silabas("pruna"), ["pru","na"])
        self.assertEqual(silabas("capsa"), ["cap","sa"])
        self.assertEqual(silabas("pingüí"), ["pin","güí"])
    
    def test_separarDigrafos(self):
        self.assertEqual(silabas("fallera"), ["fa","lle","ra"])
        self.assertEqual(silabas("escanya"), ["es","ca","nya"])
        self.assertEqual(silabas("carrer"), ["car","rer"])
        self.assertEqual(silabas("fòssil"), ["fòs","sil"])
        self.assertEqual(silabas("platja"), ["plat", "ja"])

    def test_separarEleGeminada(self):
        self.assertEqual(silabas("col·legi"), ["col","le","gi"])
        self.assertEqual(silabas("sil·labes"), ["sil","la","bes"])
    
    def test_separarDiftongos(self):
        self.assertEqual(silabas("feina"), ["fei","na"])
        self.assertEqual(silabas("sauna"), ["sau","na"])
        self.assertEqual(silabas("piscina"), ["pis","ci","na"])
        self.assertEqual(silabas("espatlla"), ["es","pat","lla"])
        self.assertEqual(silabas("jutges"), ["jut","ges"])

if __name__ == "__main__":
    unittest.main()