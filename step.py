from board import Board
class Step:
  def __init__(self, board_obj=Board()):
    self.board = board_obj
  
  def next_generation(self):
    new_grid = [list(row) for row in self.board.grid]

    for i in range(self.board.height):
      for j in range(self.board.width):
        env = self.observe(i,j) # observe the environment of the cell
        

    return new_grid

  