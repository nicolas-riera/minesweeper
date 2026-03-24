import random
from src.Cell import Cell

class GridGen:
    def __init__(self, length):
        self.grid = []
        for r in range(length):
            new_rows=[]
            for c in range(length):
                new_rows.append(Cell())
            self.grid.append(new_rows)

    def mines_spawning(self, nb, length):
        mines_amount = 0 
        while mines_amount < nb:
            r_random = random.randint(0, length-1)
            c_random = random.randint(0, length-1)

            if not self.grid[r_random][c_random].mine and not self.grid[r_random][c_random].is_dug:
                self.grid[r_random][c_random].mine = True
                mines_amount +=1




#print debug

# game = GridGen()
# game.mines_spawning()

# print("Nombre de lignes :", len(game.grid))
# print("Nombre de colonnes dans la première ligne :", len(game.grid[0]))
# sum_bomb = sum(case.mine for row in game.grid for case in row)
# print("Nombre de bombes :", sum_bomb)