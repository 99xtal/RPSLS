from gesture import Gesture

class Spock(Gesture):
    def __init__(self):
        super().__init__()
        self.name = "spock"
        self.loses_to = ["paper", "lizard"]
        self.wins_against = ["rock", "scissors"]