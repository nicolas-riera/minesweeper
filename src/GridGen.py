from Case import Case
class GridGen:
    def __init__(self):
        self.grid = []
        for r in range(8):
            new_rows=[]
            for c in range(8):
                new_rows.append(Case())
            self.grid.append(new_rows)


#print debug

game = GridGen()

print("Nombre de lignes :", len(game.grid))
print("Nombre de colonnes dans la première ligne :", len(game.grid[0]))