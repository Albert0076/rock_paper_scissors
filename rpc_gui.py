import tkinter as tk
import rpc_back


class GUI(tk.Tk):
    def __init__(self):
        super().__init__()


class StartupScreen(tk.Frame):
    def __init__(self):
        super().__init__()


class PlayerOptions(tk.Frame):
    def __init__(self, player_num: int, def_choice: str):
        super().__init__()
        self.title = tk.Label(self, text=f"Player {player_num}:")
        self.name_box_pre = tk.Label(self, text="Name:")
        self.name_box = tk.Entry(self)
        self.default_choice = tk.StringVar()
        self.default_choice.set(def_choice)
        self.type_menu = tk.OptionMenu(self, self.default_choice, *["Human", "Computer"])


    def place_widgets(self):
        pass