import random

class Difficulty:
    @staticmethod
    def easy(root):

        root.grid_lengh = 8
        root.nb_mine = random.randint(9, 11)
        root.nb_flag = root.nb_mine

    @staticmethod
    def medium(root):
        root.grid_lengh = 14
        root.nb_mine = random.randint(38, 42)
        root.nb_flag = root.nb_mine

    @staticmethod
    def hard(root):
        root.grid_lengh = 20
        root.nb_mine = random.randint(90,110)
        root.nb_flag = root.nb_mine