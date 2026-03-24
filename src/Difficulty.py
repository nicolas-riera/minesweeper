class Difficulty:
    @staticmethod
    def easy(root):

        root.grid_lengh = 8
        root.nb_mine = 10
        root.nb_flag = root.nb_mine

    @staticmethod
    def medium(root):
        root.grid_leng = 14
        root.nb_mine = 40
        root.nb_flag = root.nb_mine

    @staticmethod
    def hard(root):
        root.grid_lengh = 20
        root.nb_mine = 99
        root.nb_flag = root.nb_mine