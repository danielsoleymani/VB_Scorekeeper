class Set:
    def __init__(self, team1, team2, last_set):
        self.team1 = team1
        self.team2 = team2
        self.final_score = None
        self.last_set = last_set

    def check_win(self):
        print(self.last_set)
        if self.last_set:
            if self.team1.set_score >= 15:
                return self.team1
            if self.team2.set_score >= 15:
                return self.team2
        else:
            if self.team1.set_score >= 25:
                return self.team1
            if self.team2.set_score >= 25:
                return self.team2
        return None

    def set_win(self):
        winning_team = self.check_win()
        if winning_team is None:
            raise ValueError("No winning team yet. Cannot set the winner.")
        self.final_score = f"{self.team1.set_score}-{self.team2.set_score}"
        winning_team.set_win()
        self.team1.reset_score()
        self.team2.reset_score()
        return winning_team

    def get_final_score(self):
        return self.final_score