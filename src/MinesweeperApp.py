import customtkinter as ctk

class MinesweeperApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Budget Buddy")
        self.geometry("800x800")
        ctk.set_appearance_mode("dark")
