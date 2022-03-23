from player import Player
import random

class AI(Player):
    def __init__(self):
        super().__init__()

    def choose_gesture(self):
        cho = random.choice(self.gestures)
        self.gesture_choice = cho