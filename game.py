import time
from board import Board
from step import Step


class Game():
  def __init__(self, width=5, height=5, start_positions=[], board_class=Board):
    self.width = width
    self.height = height
    self.start_positions = start_positions
    self.board_class = board_class

    self.rounds = []

  def play(self, steps, time_interval=0.1):
    current_board = self.__gen_board(self.start_positions) # initialize the current board with the game start positions

    for i in range(steps + 1):
      self.rounds.append(current_board) # Record the current board by storing in rounds list
      self.__print_round(i, current_board) # Print out display of round and board
      time.sleep(time_interval) # execute delay to allow user to see the board

      positions = self.__get_new_positions(current_board) # generate the positions for the new board
      current_board = self.__gen_board(positions) # instantiates new board object with the specified configuration

  # Private methods
  def __print_round(self, num, board):
    print(f"step: {num}")
    print(board.pretty_grid())

  def __get_new_positions(self, board, step_class=Step):
    return step_class(board).generate_new_positions()

  def __gen_board(self, positions):
    return self.board_class(self.width, self.height, positions)


