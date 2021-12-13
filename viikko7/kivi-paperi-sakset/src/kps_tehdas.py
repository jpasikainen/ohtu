from kps_pelaaja_vs_pelaaja import KPSPelaajaVsPelaaja
from kps_tekoaly import KPSTekoaly
from kps_parempi_tekoaly import KPSParempiTekoaly

class KPSTehdas:
    def __init__(self):
        self._metodit = {}

    def lisaa_tyyppi(self, tyyppi, metodi):
        self._metodit[tyyppi] = metodi

    def pelityyppi(self, tyyppi):
        metodi = self._metodit.get(tyyppi)
        return metodi

tehdas = KPSTehdas()
tehdas.lisaa_tyyppi("a", KPSPelaajaVsPelaaja())
tehdas.lisaa_tyyppi("b", KPSTekoaly())
tehdas.lisaa_tyyppi("c", KPSParempiTekoaly())