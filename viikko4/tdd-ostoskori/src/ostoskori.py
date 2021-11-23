from tuote import Tuote
from ostos import Ostos

class Ostoskori:
    def __init__(self):
        self.kori = {}
        pass
        # ostoskori tallettaa Ostos-oliota, yhden per korissa oleva Tuote

    def tavaroita_korissa(self):
        ostoksia = 0
        for tuote in self.kori.keys():
            ostoksia += self.kori.get(tuote, 0)
        return ostoksia
        # kertoo korissa olevien tavaroiden lukumäärän
        # eli jos koriin lisätty 2 kpl tuotetta "maito", tulee metodin palauttaa 2 
        # samoin jos korissa on 1 kpl tuotetta "maito" ja 1 kpl tuotetta "juusto", tulee metodin palauttaa 2 

    def hinta(self):
        summa = 0
        for tuote in self.kori.keys():
            summa += tuote.hinta() * self.kori.get(tuote)
        return summa
        # kertoo korissa olevien ostosten yhteenlasketun hinnan

    def lisaa_tuote(self, lisattava: Tuote):
        # lisää tuotteen
        self.kori[lisattava] = self.kori.get(lisattava, 0) + 1

    def poista_tuote(self, poistettava: Tuote):
        # poistaa tuotteen
        self.kori[poistettava] = self.kori.get(poistettava, 0) - 1
        if self.kori[poistettava] == 0:
            self.kori.pop(poistettava)

    def tyhjenna(self):
        pass
        # tyhjentää ostoskorin

    def ostokset(self):
        kori_lista = []
        for tuote in self.kori.keys():
            kori_lista.append((tuote.nimi(), self.kori.get(tuote)))
        return kori_lista
        # palauttaa listan jossa on korissa olevat ostos-oliot
        # kukin ostos-olio siis kertoo mistä tuotteesta on kyse JA kuinka monta kappaletta kyseistä tuotetta korissa on
