from gesture import Gesture

class Rock(Gesture):
    def __init__(self):
        super().__init__()
        self.name = "rock"
        self.loses_to = ["paper", "spock"]
        self.wins_against = ["lizard", "scissors"]

        