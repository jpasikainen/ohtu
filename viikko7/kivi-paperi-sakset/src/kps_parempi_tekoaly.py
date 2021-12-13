from tekoaly_parannettu import TekoalyParannettu
from kps import KPS

class KPSParempiTekoaly(KPS):
    def pelaa(self):
        tekoaly = TekoalyParannettu(10)

        ekan_siirto = self._ensimmaisen_siirto()
        tokan_siirto = tekoaly.anna_siirto()

        print(f"Tietokone valitsi: {tokan_siirto}")

        while self._siirrot_ok(ekan_siirto, tokan_siirto):
            self._kirjaa_siirto(ekan_siirto, tokan_siirto)

            ekan_siirto = self._ensimmaisen_siirto()
            tokan_siirto = tekoaly.anna_siirto()

            print(f"Tietokone valitsi: {tokan_siirto}")
            tekoaly.aseta_siirto(ekan_siirto)

        self._lopeta_peli()
