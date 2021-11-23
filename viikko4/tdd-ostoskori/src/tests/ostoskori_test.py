import unittest
from ostoskori import Ostoskori
from tuote import Tuote

class TestOstoskori(unittest.TestCase):
    def setUp(self):
        self.kori = Ostoskori()

    def test_ostoskorin_hinta_ja_tavaroiden_maara_alussa(self):
        self.assertEqual(self.kori.hinta(), 0)
        self.assertEqual(self.kori.tavaroita_korissa(), 0)

    def test_yhden_tuotteen_lisaamisen_jalkeen_korissa_yksi_tavara(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)
        self.assertEqual(self.kori.tavaroita_korissa(), 1)
    
    def test_yhden_tuotteen_lisaamisen_jalkeen_korin_hinta_sama_kuin_tuotteen_hinta(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)
        self.assertEqual(self.kori.hinta(), 3)
    
    def test_kahden_eri_tuotteen_lisäämisen_jälkeen_ostoskorissa_on_kaksi_tavaraa(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)
        juusto = Tuote("Juusto", 5)
        self.kori.lisaa_tuote(juusto)
        self.assertEqual(self.kori.tavaroita_korissa(), 2)
    
    def test_kahden_eri_tuotteen_lisäämisen_jälkeen_ostoskorissa_on_oikea_hinta(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)
        juusto = Tuote("Juusto", 5)
        self.kori.lisaa_tuote(juusto)
        self.assertEqual(self.kori.hinta(), 8)
    
    def test_kahden_saman_tuotteen_lisäämisen_jälkeen_ostoskorissa_on_kaksi_tavaraa(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)
        self.kori.lisaa_tuote(maito)
        self.assertEqual(self.kori.tavaroita_korissa(), 2)
    
    def test_kahden_saman_tuotteen_lisäämisen_jälkeen_ostoskorissa_on_oikea_hinta(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)
        self.kori.lisaa_tuote(maito)
        self.assertEqual(self.kori.hinta(), 6)
    
    def test_yhden_tuotteen_lisaamisen_jalkeen_korissa_yksi_ostosolio(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)
 
        ostokset = self.kori.ostokset()
        self.assertEqual(len(ostokset), 1)
        # testaa etta metodin palauttaman listan pituus 1
    
    def test_yhden_tuotteen_lisaamisen_jalkeen_korissa_yksi_ostosolio_jolla_oikea_tuotteen_nimi_ja_maara(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)
 
        ostos = self.kori.ostokset()[0]
        self.assertEqual(ostos, ("Maito", 1))
        # testaa palautetun listan ensimmainen ostos on halutunkaltainen.

    def test_kahden_eri_tuotteen_lisaamisen_jalkeen_ostoskori_sisältaa_kaksi_ostosta(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)
        juusto = Tuote("Juusto", 5)
        self.kori.lisaa_tuote(juusto)

        ostokset = self.kori.ostokset()
        self.assertEqual(ostokset, [("Maito", 1), ("Juusto", 1)])

    def test_kahden_saman_tuotteen_lisaamisen_jalkeen_ostoskori_sisaltaa_yhden_ostoksen(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)
        self.kori.lisaa_tuote(maito)

        ostokset = self.kori.ostokset()[0]
        self.assertEqual(ostokset, ("Maito", 2))