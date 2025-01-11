from Set import Set
from tweetFactory import Tweet_Factory
from datetime import datetime


class Game:
    def __init__(self, team1, team2, number_of_sets, tweetFactory:Tweet_Factory):
        self.team1 = team1
        self.team2 = team2
        self.number_of_sets = number_of_sets
        if self.number_of_sets == 5:
            self.sets_to_win = 3
        else:
            self.sets_to_win = 2
        self.tweetFactory = tweetFactory
        self.sets = []
        self.current_set = None
        self.sets_played = 0

    def start_game(self):
        message = f"Game started between {self.team1.name} and {self.team2.name}!"
        message += self.get_date_time()
        self.tweetFactory.create_tweet(message)
        self.start_new_set()

    def end_game(self, winning_team):
        message = f"{winning_team.name} wins {self.get_leader().match_score}-{self.get_follower().match_score}.\n"
        for i, set_ in enumerate(self.sets, start=1):
            message += f"Set {i}: {set_.get_final_score()}\n"
        message += self.get_date_time()
        self.tweetFactory.create_tweet(message)

    def start_new_set(self):
        print(f"Sets played: {self.sets_played}, Total sets: {self.number_of_sets}")
        if self.sets_played + 1 == self.number_of_sets:
            self.current_set = Set(self.team1, self.team2, True)
        else:
            self.current_set = Set(self.team1, self.team2, False)

    def end_set(self, winning_team):
        self.sets.append(self.current_set)
        self.sets_played += 1
        if self.check_win() is None:
            if self.get_leader() is None:
                message = (f"{winning_team.name} wins set #{self.sets_played}: {self.current_set.get_final_score()}. Teams are tied "
                           f"{self.team1.match_score}-{self.team2.match_score} going into set #{self.sets_played + 1}")
            else:
                message = (f"{winning_team.name} wins set #{self.sets_played}: {self.current_set.get_final_score()}. "
                           f"{self.get_leader().name} leads {self.get_leader().match_score}-{self.get_follower().match_score} "
                           f"going into set #{self.sets_played + 1}")
            message += self.get_date_time()
            self.tweetFactory.create_tweet(message)
            self.start_new_set()
            return True
        else:
            self.end_game(self.check_win())
            return False 

    def check_win(self):
        if self.team1.match_score == self.sets_to_win:
            return self.team1
        elif self.team2.match_score == self.sets_to_win:
            return self.team2
        return None

    def get_leader(self):
        if self.team1.match_score > self.team2.match_score:
            return self.team1
        elif self.team1.match_score < self.team2.match_score:
            return self.team2
        return None

    def get_follower(self):
        if self.team1.match_score < self.team2.match_score:
            return self.team1
        elif self.team1.match_score > self.team2.match_score:
            return self.team2
        return None
    
    def get_date_time(self):
        current_time = "\n\nTime: " + datetime.now().strftime("%I:%M %p")
        return current_time