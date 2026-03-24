class Cell:
    def __init__(self):
        self.mine = False
        self.flag = False
        self.questionmark = False
        self.is_dug = False
        self.surrounding_bombs = 0 #0 to 8 (9)
    
    # def grid(self, rows, columns):
    #     self.column = columns
    #     self.row = rows

        # grid = []

        # def grid(self):
            
