from player import Player
import random

class AI(Player):
    def __init__(self):
        super().__init__()
        self.name = "Al the AI"

    def choose_gesture(self):
        cho = random.choice(self.gestures)
        self.gesture_choice = cho
        print(f'{self.name} picked {cho}')
