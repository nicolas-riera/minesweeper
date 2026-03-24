import customtkinter as ctk

from src.GridGen import GridGen
from src.GameRendering import GameRendering
from src.Difficulty import Difficulty

class Game:
    def __init__(self, root):
        self.root = root
        self.first_launch = True
        self.seconds = -1
        self.timer_running = False

        self.grid = GridGen(self.root.grid_length)

        GameRendering.game_rendering(self)

    def spawn_mines(self):
        self.first_launch = False
        self.grid.mines_spawning(self.root.nb_mines, self.root.grid_length)

    def restart(self):
        if 9 <= self.root.nb_mines <= 11:
            Difficulty.easy(self.root)
        elif 38 <= self.root.nb_mines <= 42:
            Difficulty.medium(self.root)
        else:
            Difficulty.hard(self.root)
        self.root.page_switcher("game")

    def exit_to_main_menu(self):
        self.root.page_switcher("menu")