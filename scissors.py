from gesture import Gesture

class Scissors(Gesture):
    def __init__(self):
        super().__init__()
        self.name = "scissors"
        self.loses_to = ["rock", "spock"]
        self.wins_against = ["paper", "lizard"]