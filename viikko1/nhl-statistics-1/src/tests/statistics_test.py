import unittest
from statistics import Statistics
from player import Player

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]

class TestStatistics(unittest.TestCase):
    def setUp(self):
        # annetaan Statistics-luokan oliolle "stub"-luokan olio
        self.statistics = Statistics(
            PlayerReaderStub()
        )

    def test_tiimit_luotu_oikein(self):
        players = []
        for player in self.statistics.team("EDM"):
            players.append(str(player))

        self.assertEqual(players, ['Semenko EDM 4 + 12 = 16', 'Kurri EDM 37 + 53 = 90', 'Gretzky EDM 35 + 89 = 124'])

    def test_hae_pelaajaa(self):
        self.assertEqual(str(self.statistics.search("Semenko")), "Semenko EDM 4 + 12 = 16")
    
    def test_hae_olematonta_pelaajaa(self):
        self.assertEqual(self.statistics.search("wasd"), None)
    
    def test_hae_top_scorers(self):
        players = []
        for player in self.statistics.top_scorers(1):
            players.append(str(player))

        self.assertEqual(players, ['Gretzky EDM 35 + 89 = 124', 'Lemieux PIT 45 + 54 = 99'])
    
    def test_hae_top_scorers_negatiivinen_luku(self):
        players = []
        for player in self.statistics.top_scorers(-1):
            players.append(str(player))

        self.assertEqual(players, [])

