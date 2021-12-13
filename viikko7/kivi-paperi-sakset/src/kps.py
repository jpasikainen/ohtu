from tuomari import Tuomari

class KPS:
	def __init__(self):
		self._tuomari = Tuomari()

	def _ensimmaisen_siirto(self):
	  return input("Ensimmäisen pelaajan siirto: ")

	def _onko_ok_siirto(self, siirto):
		return siirto == "k" or siirto == "p" or siirto == "s"

	def _kirjaa_siirto(self, ekan_siirto, tokan_siirto):
		self._tuomari.kirjaa_siirto(ekan_siirto, tokan_siirto)
		print(self._tuomari)
	
	def _lopeta_peli(self):
		print("Kiitos!")
		print(self._tuomari)
	
	def _siirrot_ok(self, ekan_siirto, tokan_siirto):
		return self._onko_ok_siirto(ekan_siirto) and self._onko_ok_siirto(tokan_siirto)
