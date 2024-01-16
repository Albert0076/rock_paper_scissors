import time
import tkinter as tk
import rpc_back
RULES = rpc_back.RULES
#Rock: U+270A
#Scissors: U+2702
#Paper: U+2709


class GUI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title = "Rock Paper Scissors"
        self.startup = StartupScreen(self)
        self.game_frame = GameFrame()

        self.place_widgets()

    def place_widgets(self):
        self.startup.grid(row=0, column=0)

    def start_game(self, names, types, rules, rounds):
        pass


class StartupScreen(tk.Frame):
    def __init__(self, master):
        super().__init__()
        self.p1_options = PlayerOptions(1, "Human")
        self.p2_options = PlayerOptions(2, "Computer")
        self.startup_options = StartupOptions()
        self.start_button = StartButton(self)

        self.place_widgets()

    def place_widgets(self):
        self.p1_options.grid(row=0, column=0)
        self.p2_options.grid(row=0, column=1)
        self.startup_options.grid(row=1, column=0, sticky="WE")
        self.start_button.grid(row=1, column=1)

    def start_game(self):
        names = (self.p1_options.player_name.get(), self.p2_options.player_name.get())
        types = (self.p1_options.default_choice.get(), self.p2_options.player_name.get())
        rules = self.startup_options.rules_menu_default.get()
        rounds = int(self.startup_options.user_rounds.get())
        self.master.start_game(names, types, rules, rounds)


class PlayerOptions(tk.Frame):
    def __init__(self, player_num: int, def_choice: str):
        super().__init__()
        self.title = tk.Label(self, text=f"Player {player_num}:")
        self.name_box_pre = tk.Label(self, text="Name:")
        self.player_name = tk.StringVar()
        self.player_name.set(f"player{player_num}")
        self.name_box = tk.Entry(self, textvariable=self.player_name)
        self.default_choice = tk.StringVar()
        self.default_choice.set(def_choice)
        self.type_menu = tk.OptionMenu(self, self.default_choice, *["Human", "Computer"])

        self.place_widgets()

    def place_widgets(self):
        settings = {'padx': 10, 'pady': 10}
        self.title.grid(row=0, column=0, sticky="WE", **settings)
        self.name_box_pre.grid(row=1, column=0, **settings)
        self.name_box.grid(row=1, column=1, **settings)
        self.type_menu.grid(row=2, column=0, sticky="WE", **settings)


class StartupOptions(tk.Frame):
    def __init__(self):
        super().__init__()
        self.rules_menu_default = tk.StringVar()
        self.rules_menu_default.set("Rules")
        self.rules_menu = tk.OptionMenu(self, self.rules_menu_default, *["RPS", "RPSLS"])
        self.user_rounds = tk.StringVar()
        self.max_rounds_text = tk.Label(self, text="Max Rounds:")
        self.max_rounds_input = tk.Entry(self, textvariable=self.user_rounds)

        self.place_widgets()

    def place_widgets(self):
        settings = {'padx': 10, 'pady': 10}
        self.rules_menu.grid(row=1, column=1, **settings)
        self.max_rounds_text.grid(row=2, column=0, **settings)
        self.max_rounds_input.grid(row=2, column=1, **settings)


class StartButton(tk.Frame):
    def __init__(self, master):
        super().__init__()
        self.master = master
        self.startup_button = tk.Button(self, text="Start Game", command=self.start_game)

        self.place_widgets()

    def place_widgets(self):
        self.startup_button.grid(row=0, column=0)

    def start_game(self):
        self.master.start_game()


class GameFrame(tk.Frame):
    def __init__(self):
        super().__init__()
        self.game_back = rpc_back.Game()
        self.names = ()

    def setup(self, names, types, rules, rounds):
        for i in range(len(names)):
            if types[i] == "Human":
                self.game_back.add_human_player(names[i])

            else:
                self.game_back.add_computer_player()

        self.game_back.change_rules(rules.lower())
        self.game_back.set_max_rounds(rounds)
        self.names = names

    def run_game(self):
        while self.game_back.current_round < self.game_back.max_rounds:



class ResultFrame(tk.Frame):
    def __init__(self, controller):
        super().__init__()
        self.controller = controller
        p1_title = tk.Label(self, text=self.controller.names[0])
        p1_title = tk.Label(self, text=self.controller.names[1])


class MoveFrame(tk.Frame):
    def __init__(self, controller, player, rules):
        super().__init__()
        self.controller = controller
        self.player = player
        self.rules = rules
        for rule in RULES[self.rules]:

if __name__ == "__main__":
    gui = GUI()
    gui.mainloop()
