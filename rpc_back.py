import random

RULES = {"rps": {"rock": ("scissors",),
                 "scissors": ("paper",),
                 "paper": ("rock",),
                 },
         "rpsls": {"rock": ("scissors", "lizard"),
                   "scissors": ("paper", "lizard"),
                   "paper": ("rock", "spock"),
                   "lizard": ("paper", "spock"),
                   "spock": ("rock", "scissors"),
                   },
         }


class PlayerObject:
    def __init__(self, name, rules=None):
        if rules is None:
            rules = RULES["rps"]
        self.rules = rules
        if name.lower() in self.rules.keys():
            self.name = name.lower()

        else:
            self.name = None

    def __repr__(self):
        return f"PlayerObject({self.name})"

    def __gt__(self, other):
        return other.name in self.rules[self.name]

    def __eq__(self, other):
        return self.name == other.name

    def random_object(self):
        return random.choice(list(self.rules.keys()))


class Player:
    def __init__(self, name):
        self.name = name
        self.score = 0
        self.current_object = None

    def reset_object(self):
        self.current_object = None

    def win_round(self):
        self.score += 1

    def __repr__(self):
        return f"Player(Name: {self.name}, Score: {self.score}"


class HumanPlayer(Player):
    def choose_object(self, choice):
        self.current_object = PlayerObject(choice)


class ComputerPlayer(Player):
    def __init__(self, name):
        super().__init__(name)
        self.name = "Computer"
        self.current_object = PlayerObject("Computer")

    def choose_object(self):
        self.current_object.random_object()


class Game:
    def __init__(self):
        self.current_round = 0
        self.max_rounds = 10
        self.players = []
        self.round_result = None
        self.round_winner = None

    def add_human_player(self, name):
        self.players.append(HumanPlayer(name))

    def add_computer_player(self):
        self.players.append(ComputerPlayer("Computer"))

    def set_max_rounds(self, rounds):
        if isinstance(rounds, int):
            self.max_rounds = rounds

    def find_winner(self):
        player_1 = self.players[0]
        player_2 = self.players[1]
        if player_1.current_object is not None and player_2.current_object is not None:
            if player_1.current_object == player_2.current_object:
                self.round_result = "Draw"

            elif player_1.current_object > player_2.current_object:
                self.round_winner = player_1.name
                player_1.win_round()
                self.round_result = "Won"
            else:
                self.round_winner = player_2.name
                player_2.win_wound()
                self.round_result = "Won"

    def next_round(self):
        self.current_round += 1
        self.round_result = None
        self.round_winner = None
        for player in self.players:
            player.reset_object()

    def is_finished(self):
        return self.current_round >= self.max_rounds

    def reset(self):
        self.current_round = 0
        for player in self.players:
            player.score = 0

    def report_round(self):
        player_1 = self.players[0]
        player_2 = self.players[1]
        message = (f"{player_1.name} chose {player_1.current_object}.\n"
                   f"{player_2.name} chose {player_2.current_object}.\n"
                   f"The round resulted in a {self.round_result}.\n")

        if self.round_winner == player_1.name:
            message += f"{player_1.name} won the round.\n"

        elif self.round_winner == player_2.name:
            message += f"{player_2.name} won the round.\n"  #

        return message

    def report_score(self):
        return (f"{self.players[0].name} has {self.players[0].score} points.\n"
                f"{self.players[1].name} has {self.players[1].score} points")

    def report_winner(self):
        message = ""
        if self.players[0].score == self.players[1].score:
            message = f"The game is a draw."

        elif self.players[0].score > self.players[1].score:
            message = f"{self.players[0].name} wins the game"

        else:
            message = f"{self.players[1].name} wins the game"

