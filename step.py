from board import Board
class Step:
  def __init__(self, board_obj=Board()):
    self.board = board_obj
  
  def generate_new_positions(self):
    # new_grid = [list(row) for row in self.board.grid]
    new_positions = []

    for i in range(self.board.height):
      for j in range(self.board.width):
        env = self.__observe(i,j) # observe the environment of the cell
        num_living = self.__count_living(env) # Counts number of living neighbours
        cell = self.board.grid[i][j]
        # new_grid[i][j] = self.judge(cell, num_living) # judge if cell lives or dies and save to new grid
        if self.__judge(cell, num_living): # judge if cell lives or dies and save to new grid
          new_positions.append([i,j])

    return new_positions

  def __observe(self, i, j):
    g = self.board.grid
    rw = 1 - self.board.width
    rh = 1 - self.board.height
    return [ 
      [g[i-1][j-1], g[i-1][j], g[i-1][j+rw]],
      [g[i][j-1], None, g[i][j+rw]],
      [g[i+rh][j-1], g[i+rh][j], g[i+rh][j+rw]]
    ]

  def __count_living(self, env):
    return sum(line.count(1) for line in env)

  def __judge(self, cell, num_living):
    if cell == 1: # cell in question is alive
      if num_living < 2 or num_living > 3: # Dies of underpopulation / overpopulation
        return 0
      else: # 2 or 3 neighbours == survival
        return 1

    # cell in question is not alive
    if num_living == 3: # Birth condition
      return 1
    else: # stay dead
      return 0