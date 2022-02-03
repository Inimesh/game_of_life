from unittest.mock import Mock
from step import Step
from board import Board




def test_next_gen():
  """Step.next_generation should return a new grid according to the rules of the game"""
  start_positions = [
    [1,2],
    [2,0],[2,2],
    [3,1],[3,2]
  ]
  board = Board(5, 5, start_positions)
  step = Step(board)
  assert step.next_generation() == [
      [0, 0, 0, 0, 0], 
      [0, 1, 0, 0, 0], 
      [0, 0, 1, 1, 0], 
      [0, 1, 1, 0, 0], 
      [0, 0, 0, 0, 0]
    ]

  