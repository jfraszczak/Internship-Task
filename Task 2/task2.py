# TASK 2


class IslandsCounter:
    def __init__(self, islands_map):
        self.map = islands_map
        self.rows = len(self.map)
        self.columns = len(self.map[0])
        self.visited_islands = [[0 for _ in range(self.columns)] for _ in range(self.rows)]
        self.number_of_islands = 0

    def expandIsland(self, row, col):
        expanded_cells = [(row, col)]
        self.visited_islands[row][col] = 1
        for cell in expanded_cells:
            print(cell)
            row_cell = cell[0]
            col_cell = cell[1]
            if row_cell >= 1:
                if self.map[row_cell - 1][col_cell] == 1 and self.visited_islands[row_cell - 1][col_cell] == 0:
                    self.visited_islands[row_cell - 1][col_cell] = 1
                    expanded_cells.append((row_cell - 1, col_cell))

            if row_cell < self.rows - 1:
                if self.map[row_cell + 1][cell[1]] == 1 and self.visited_islands[row_cell + 1][col_cell] == 0:
                    self.visited_islands[row_cell + 1][col_cell] = 1
                    expanded_cells.append((row_cell + 1, col_cell))

            if col_cell >= 1:
                if self.map[row_cell][col_cell - 1] == 1 and self.visited_islands[row_cell][col_cell - 1] == 0:
                    self.visited_islands[row_cell][col_cell - 1] = 1
                    expanded_cells.append((row_cell, col_cell - 1))

            if col_cell < self.columns - 1:
                if self.map[row_cell][col_cell + 1] == 1 and self.visited_islands[row_cell][col_cell + 1] == 0:
                    self.visited_islands[row_cell][col_cell + 1] = 1
                    expanded_cells.append((row_cell, col_cell + 1))

    def showVisitedIslands(self):
        for row in self.visited_islands:
            print(row)

    def count(self):
        for row in range(self.rows):
            for col in range(self.columns):
                if self.visited_islands[row][col] == 1:
                    continue
                if self.map[row][col] == 1:
                    self.number_of_islands += 1
                    self.expandIsland(row, col)
                    self.showVisitedIslands()

    def getNumberOfIslands(self):
        return self.number_of_islands
