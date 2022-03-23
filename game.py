from player import Player
from ai import AI

class Game:
    def __init__(self):
        self.player = Player()
        self.opponent = None
        self.combinations = {"rockrock": None,
                            "rockpaper": self.opponent,
                            "rockscissors": self.player,
                            "rocklizard": self.player,
                            "rockspock": self.opponent,
                            "paperrock": self.player,
                            "paperpaper": None,
                            "paperscissors": self.opponent,
                            "paperlizard": self.opponent,
                            "paperspock": self.player,
                            "scissorsrock": self.opponent,
                            "scissorspaper": self.player,
                            "scissorsscissors": None,
                            "scissorslizard": self.player,
                            "scissorsspock": self.opponent,
                            "lizardrock": self.opponent,
                            "lizardpaper": self.player,
                            "lizardscissors": self.opponent,
                            "lizardlizard": None,
                            "lizardspock": self.player,
                            "spockrock": self.player,
                            "spockpaper": self.opponent,
                            "spockscissors": self.player,
                            "spocklizard": self.opponent,
                            "spockspock": None}
    
    def run_game(self):
        self.display_welcome()
        self.choose_game_mode()
        self.battle()
        self.display_winner()

    def display_welcome(self):
        print("Hello! Welcome to Rock, Paper, Scissors, Lizard, Spock")

    def battle(self):
        self.player.choose_gesture()
        self.opponent.choose_gesture()
        
        # self.player.gesture_choice    self.opponent.gesture_choice

    def choose_winner(self):
        opt1 = self.player.gesture_choice
        opt2 = self.opponent.gesture_choice

        

    def player_turn(self):
        pass

    def opponent_turn(self):
        pass

    def choose_game_mode(self):
        game_choice = input("Would you like a single player(1) or multiplayer game(2)? Type 1 or 2")
        if game_choice == "1":
            self.opponent = AI()
        elif game_choice == "2":
            self.opponent = Player()

    def display_winner(self):
        pass

rpsls = Game()
rpsls.run_game()