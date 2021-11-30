class TennisGame:
    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.m_score1 = 0
        self.m_score2 = 0
        self.score_name = {
            0: "Love",
            1: "Fifteen",
            2: "Thirty",
            3: "Forty"
        }
        self.max_score = 4

    def won_point(self, player_name):
        if player_name == "player1":
            self.m_score1 = self.m_score1 + 1
        else:
            self.m_score2 = self.m_score2 + 1

    def score_even(self):
        score = self.score_name.get(self.m_score1, "Deuce")
        if score != "Deuce":
            score += "-All"
        return score

    def advantage_or_victory(self):
        minus_result = self.m_score1 - self. m_score2
        # Player 1
        if minus_result > 0:
            if minus_result == 1:
                return "Advantage player1"
            return "Win for player1"
        # Player 2
        else:
            if minus_result == -1:
                return "Advantage player2"
            return "Win for player2"

    def get_score(self):
        # Even
        if self.m_score1 == self.m_score2:
            return self.score_even()

        # Advantage or victory
        if self.m_score1 >= self.max_score or self.m_score2 >= self.max_score:
            return self.advantage_or_victory()
        
        # Normal scoring
        return self.score_name.get(self.m_score1) + "-" + self.score_name.get(self.m_score2)