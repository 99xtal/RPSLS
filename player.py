class Player:
    def __init__(self, name):
        self.gestures = ['rock', 'paper', 'scissors', 'lizard', 'spock']
        self.gesture_choice = None
        self.name = name
        self.score = 0

    def choose_gesture(self):
        # input choice function
        while True:
            for each in self.gestures:
                print(each)
            choice = input("Choose an option")
            if choice in self.gestures:
                self.gesture_choice = choice
                break
            else:
                print("Oops! Please type one of the options!")