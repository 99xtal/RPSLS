class Player:
    def __init__(self):
        self.gestures = ['rock', 'paper', 'scissors', 'lizard', 'spock']
        self.gesture_choice = None
        self.name = None
        self.score = 0

    def choose_gesture(self):
        # input choice function
        while True:
            print("\nOPTIONS:")
            for each in self.gestures:
                print(each)
            choice = input(f"\n{self.name}, choose an option: ").lower()
            if choice in self.gestures:
                self.gesture_choice = choice
                break
            else:
                print("Oops! Please type one of the options!")

    def set_name(self):
        self.name = input("Name: ")