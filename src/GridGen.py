import random
from Case import Case

class GridGen:
    def __init__(self):
        self.grid = []
        for r in range(8):
            new_rows=[]
            for c in range(8):
                new_rows.append(Case())
            self.grid.append(new_rows)

    def mines_spawning(self):
        mines_amount = 0 #up to three for testing purposes
        while mines_amount < 3:
            r_random = random.randint(0, 7)
            c_random = random.randint(0, 7)

            if not self.grid[r_random][c_random].mine:
                self.grid[r_random][c_random].mine = True
                mines_amount +=1




#print debug

game = GridGen()
game.mines_spawning()

print("Nombre de lignes :", len(game.grid))
print("Nombre de colonnes dans la première ligne :", len(game.grid[0]))
sum_bomb = sum(case.mine for row in game.grid for case in row)
print("Nombre de bombes :", sum_bomb)