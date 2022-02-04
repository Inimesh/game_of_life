import unittest
from board import Board

class TestBoard(unittest.TestCase):

  def setUp(self):
    self.board = Board(5, 5)

  def tearDown(self):
    pass

  def test_pretty_grid(self):
    """pretty_grid() should return a formatted string of self.grid"""
    self.assertEqual(self.board.pretty_grid(), "0 0 0 0 0\n0 0 0 0 0\n0 0 0 0 0\n0 0 0 0 0\n0 0 0 0 0")

  def test_populate(self):
    """populate() should populate self.grid with ones as the specified 2D indices [[i,j], [i,j]...]"""
    positions = [ # Glider config
      [1,2],
      [2,0],[2,2],
      [3,1],[3,2]
    ]
    self.board.populate(positions)
    self.assertEqual(self.board.pretty_grid(), "0 0 0 0 0\n0 0 1 0 0\n1 0 1 0 0\n0 1 1 0 0\n0 0 0 0 0")
    
if __name__ == '__main__':
  unittest.main()



