from unittest.mock import Mock
from step import Step
from board import Board


start_positions = [
  [1,2],
  [2,0],[2,2],
  [3,1],[3,2]
]

def test_next_gen():
  """Step.next_generation should return a new grid according to the rules of the game"""
  board = Board(5, 5, start_positions)
  step = Step(board)
  assert step.next_generation() == [
      [0, 0, 0, 0, 0], 
      [0, 1, 0, 0, 0], 
      [0, 0, 1, 1, 0], 
      [0, 1, 1, 0, 0], 
      [0, 0, 0, 0, 0]
    ]

def test_observe_environment():
  """Step.observe should return a 3x3 grid (2D array) of the neighbours of the cell being observed.
  The cell being observed should be counted as None type"""
  board = Board(5, 5, start_positions)
  step = Step(board)
  assert step.observe(2,2) == [
    [0, 1, 0],
    [0, None, 0],
    [1, 1, 0]
  ]

def test_num_living():
    """Step.count_living(env) should return the number of living cells (cell == 1)"""
    board = Board(5, 5, start_positions)
    step = Step(board)
    env = step.observe(2,2)
    assert step.count_living(env) == 3

def test_judge():
  """Step.judge should return the outcome of a cell based on the number of its living neighbours"""
  board = Board(5, 5, start_positions)
  step = Step(board)
  # cell is alive
  cell = 1
  assert step.judge(cell, 0) == 0
  assert step.judge(cell, 1) == 0
  assert step.judge(cell, 2) == 1
  assert step.judge(cell, 3) == 1
  assert step.judge(cell, 4) == 0
  assert step.judge(cell, 5) == 0
  assert step.judge(cell, 6) == 0

  # cell is not alive
  cell = 0
  assert step.judge(cell, 0) == 0
  assert step.judge(cell, 1) == 0
  assert step.judge(cell, 2) == 0
  assert step.judge(cell, 3) == 1
  assert step.judge(cell, 4) == 0
  assert step.judge(cell, 5) == 0
  assert step.judge(cell, 6) == 0
  
