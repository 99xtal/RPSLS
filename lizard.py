from gesture import Gesture

class Lizard(Gesture):
    def __init__(self):
        super().__init__()
        self.name = "lizard"
        self.loses_to = ["rock", "scissors"]
        self.wins_against = ["paper", "spock"]