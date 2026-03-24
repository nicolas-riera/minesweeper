import customtkinter as ctk
import sys

from src.Menu import Menu

class MinesweeperApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Minesweeper")
        self.geometry("800x800")
        ctk.set_appearance_mode("dark")

        self.container = ctk.CTkFrame(master=self)
        self.container.pack(fill="both", expand=True)

        Menu.menu(self)

    def clear_container(self):
        for widget in self.container.winfo_children():
            widget.destroy()

    def start_game(self):
        
        self.clear_container()

        
    def exit(self):
        sys.exit()
