from src.GridGen import GridGen
from src.GameRendering import GameRendering

class Game:
    def __init__(self, root):
        self.root = root
        self.first_launch = True

        self.grid = GridGen(self.root.grid_lengh)
        GameRendering.game_rendering(self)

    def spawn_mines(self):
        self.first_launch = False
        self.grid.mines_spawning(self.root.nb_mines, self.root.grid_lengh)

    def is_a_mine(self,  mine):
        pass

    def is_empty(self, empty_case):
        pass