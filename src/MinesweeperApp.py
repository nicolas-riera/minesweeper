import customtkinter as ctk
import sys

from src.Menu import Menu
from src.Game import Game

class MinesweeperApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Minesweeper")
        self.geometry("800x800")
        ctk.set_appearance_mode("dark")

        self.container = ctk.CTkFrame(master=self)
        self.container.pack(fill="both", expand=True)

        self.page_switcher("menu")

    def clear_container(self):
        for widget in self.container.winfo_children():
            widget.destroy()

    def start_game(self):
        
        self.clear_container()

        self.game = Game(self)

    def page_switcher(self, page):

        self.clear_container()

        match page:
            case "game":
                self.start_game()
            case "menu":
                Menu.menu(self)
            case _:
                self.exit()
        
    def exit(self):
        sys.exit()
