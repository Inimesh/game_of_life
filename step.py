from board import Board
class Step:
  def __init__(self, board_obj=Board()):
    self.board = board_obj
  
  def next_generation(self):
    new_grid = [list(row) for row in self.board.grid]

    for i in range(self.board.height):
      for j in range(self.board.width):
        env = self.observe(i,j) # observe the environment of the cell
        num_living = self.count_living(env) # Counts number of living neighbours

    return new_grid

  def observe(self, i, j):
    g = self.board.grid
    rw = 1 - self.board.width
    rh = 1 - self.board.height
    return [ 
      [g[i-1][j-1], g[i-1][j], g[i-1][j+rw]],
      [g[i][j-1], None, g[i][j+rw]],
      [g[i+rh][j-1], g[i+rh][j], g[i+rh][j+rw]]
    ]

  def count_living(self, env):
    return sum(line.count(1) for line in env)