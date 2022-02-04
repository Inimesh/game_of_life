import unittest
from step import Step
from board import Board

class TestStep(unittest.TestCase):

  def setUp(self):
    self.start_positions = [
      [1,2],
      [2,0],[2,2],
      [3,1],[3,2]
    ]
    self.step = Step(Board(5, 5, self.start_positions))

  def tearDown(self):
    pass

  def test_next_gen(self):
    """Step.next_generation should return a new grid according to the rules of the game"""
    self.assertEqual(self.step.next_generation(), [
        [0, 0, 0, 0, 0], 
        [0, 1, 0, 0, 0], 
        [0, 0, 1, 1, 0], 
        [0, 1, 1, 0, 0], 
        [0, 0, 0, 0, 0]
      ])

  def test_observe(self):
    """Step.observe should return a 3x3 grid (2D array) of the neighbours of the cell being observed.
    The cell being observed should be counted as None type"""
    self.assertEqual(self.step.observe(2,2), [
      [0, 1, 0],
      [0, None, 0],
      [1, 1, 0]
    ])

  def test_count_living(self):
      """Step.count_living(env) should return the number of living cells (cell == 1)"""
      self.env = [
        [0, 1, 0],
        [0, None, 0],
        [1, 1, 0]
      ]
      self.assertEqual(self.step.count_living(self.env), 3)

  def test_judge(self):
    """Step.judge should return the outcome of a cell based on the number of its living neighbours"""
    # cell is alive
    self.cell = 1
      
    self.assertEqual(self.step.judge(self.cell, 0), 0)
    self.assertEqual(self.step.judge(self.cell, 1), 0)
    self.assertEqual(self.step.judge(self.cell, 2), 1)
    self.assertEqual(self.step.judge(self.cell, 3), 1)
    self.assertEqual(self.step.judge(self.cell, 4), 0)
    self.assertEqual(self.step.judge(self.cell, 5), 0)
    self.assertEqual(self.step.judge(self.cell, 6), 0)

    # cell is not alive
    self.cell = 0
    self.assertEqual(self.step.judge(self.cell, 0), 0)
    self.assertEqual(self.step.judge(self.cell, 1), 0)
    self.assertEqual(self.step.judge(self.cell, 2), 0)
    self.assertEqual(self.step.judge(self.cell, 3), 1)
    self.assertEqual(self.step.judge(self.cell, 4), 0)
    self.assertEqual(self.step.judge(self.cell, 5), 0)
    self.assertEqual(self.step.judge(self.cell, 6), 0)
    
if __name__ == "__main__":
  unittest.main()