from kps import KPS

class KPSPelaajaVsPelaaja(KPS):
    def pelaa(self):
        ekan_siirto = self._ensimmaisen_siirto()
        tokan_siirto = self._toisen_siirto()

        while self._siirrot_ok(ekan_siirto, tokan_siirto):
            self._kirjaa_siirto(ekan_siirto, tokan_siirto)

            ekan_siirto = self._ensimmaisen_siirto()
            tokan_siirto = self._toisen_siirto()

        self._lopeta_peli()
    
    def _toisen_siirto(self):
        return input("Toisen pelaajan siirto: ")