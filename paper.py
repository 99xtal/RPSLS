from gesture import Gesture

class Paper(Gesture):
    def __init__(self):
        super().__init__()
        self.name = "paper"
        self.loses_to = ["lizard", "scissors"]
        self.wins_against = ["rock", "spock"]