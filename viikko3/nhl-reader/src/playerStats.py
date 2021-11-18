class PlayerStats:
    def __init__(self, reader):
        self.reader = reader

    def top_scorers_by_nationality(self, nationality):
        players = self.reader.get_players()
        players.sort(key = lambda x: x.assists + x.goals, reverse=True)
        return filter(lambda x: x.nationality == nationality, players)

