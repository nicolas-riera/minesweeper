import random
from src.Cell import Cell

surrounding = [
                (-1, -1), (0,-1), (1,-1),
                (-1,0), (-1,1), (0,1),
                (1,1),(1,0)
            ]

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
    
    def calculate_sourrounding_bombs(self, length):
        for i in range(length):
            for j in range(length):
                if not self.grid[i][j].mine:
                    for s in surrounding:
                        if length-1 >= i + s[0] >= 0 and length-1 > j + s[1] > 0:
                            if self.grid[i+s[0]][j+s[1]].mine:
                                self.grid[i][j].surrounding_bombs += 1
        

    def reveal_empty_cells(self, row, column, length):
        if row < 0 or row >= length or column < 0 or column >= length:
            return
        
        cell = self.grid[row][column]

        if cell.mine or cell.flag or cell.is_dug: 
            return
        
        cell.is_dug = True

        if cell.surrounding_bombs == 0:
            
            for sr, sc in surrounding:
                self.reveal_empty_cells(row+sr, column+sc, length) #recursive as the function calls itself 