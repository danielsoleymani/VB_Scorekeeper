class Team:
    def __init__(self, name, primary_color):
        self.name = name
        self.primary_color = primary_color
        self.match_score = 0
        self.set_score = 0

    def increase_score(self):
        self.set_score += 1

    def edit_set_score(self, score):
        self.set_score = score

    def edit_match_score(self, score):
        self.match_score = score

    def reset_score(self):
        self.set_score = 0

    def set_win(self):
        self.match_score += 1
        self.reset_score()