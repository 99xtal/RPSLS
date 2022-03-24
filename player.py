class Player:
    def __init__(self, name):
        self.gestures = ['rock', 'paper', 'scissors', 'lizard', 'spock']
        self.gesture_choice = None
        self.name = name
        self.score = 0

    def choose_gesture(self):
        pass