from board import Board

def test_pretty_grid():
  """pretty_grid() should return a formatted string of self.grid"""
  board = Board(5, 5)
  assert board.pretty_grid() == "0 0 0 0 0\n0 0 0 0 0\n0 0 0 0 0\n0 0 0 0 0\n0 0 0 0 0"

def test_populate():
  """populate() should populate self.grid with ones as the specified 2D indices [[i,j], [i,j]...]"""
  board = Board(5, 5)

  positions = [ # Glider config
    [1,2],
    [2,0],[2,2],
    [3,1],[3,2]
  ]
  board.populate(positions)
  assert board.pretty_grid() == "0 0 0 0 0\n0 0 1 0 0\n1 0 1 0 0\n0 1 1 0 0\n0 0 0 0 0"
  




