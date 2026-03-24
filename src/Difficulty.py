import random

class Difficulty:
    @staticmethod
    def easy(root):

        root.grid_lengh = 8
        root.nb_mines = root.nb_flag = random.randint(9, 11)

    @staticmethod
    def medium(root):
        root.grid_lengh = 14
        root.nb_mines = root.nb_flag = random.randint(38, 42)

    @staticmethod
    def hard(root):
        root.grid_lengh = 20
        root.nb_mines = root.nb_flag = random.randint(90,110)