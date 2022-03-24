from human import Human
from ai import AI
from rock import Rock

class Game:
    def __init__(self):
        self.player = Human("Player 1")
        self.opponent = Human("Player 2")
    
    def run_game(self):
        self.display_welcome()
        self.choose_game_mode()
        self.battle()
        self.display_winner()

    def display_welcome(self):
        print("Hello! Welcome to Rock, Paper, Scissors, Lizard, Spock")

    def battle(self):
        while self.player.score < 2 and self.opponent.score < 2:
            self.player.choose_gesture()
            self.opponent.choose_gesture()
            winner = self.choose_winner()
            self.print_winner(winner)

    def print_winner(self, winner):
        if winner == None:
            print(f'\nNobody wins!')
        else:
            print(f'\n{winner.name} won the round')
            winner.score += 1
            print(f'{winner.name} has a score of {winner.score}')

    def choose_winner(self):
        player_gesture = self.player.gesture_choice
        opponent_gesture = self.opponent.gesture_choice

        if opponent_gesture.name in player_gesture.loses_to:
            return self.opponent
        elif opponent_gesture.name in player_gesture.wins_against:
            return self.player
        else:
            return None
    
    def choose_game_mode(self):
        while True:
            game_choice = input("Would you like a single player(1) or multiplayer game(2)? Type 1 or 2: ")
            self.player.set_name()
            if game_choice == "1":
                self.opponent = AI()
                break
            elif game_choice == "2":
                self.opponent.set_name()
                break
            else:
                print("Please choose (1) or (2)")

    def display_winner(self):
        if self.player.score == 2:
            print(f"{self.player.name} wins!\n")
        if self.opponent.score == 2:
            print(f"{self.opponent.name} wins!\n")