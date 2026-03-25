import random

class Difficulty:
    @staticmethod
    def easy(root):
        root.grid_length = 8
        root.nb_mines = root.nb_flags = random.randint(9, 11)

    @staticmethod
    def medium(root):
        root.grid_length = 14
        root.nb_mines = root.nb_flags = random.randint(38, 42)

    @staticmethod
    def hard(root):
        root.grid_length = 20
        root.nb_mines = root.nb_flags = random.randint(90,110)