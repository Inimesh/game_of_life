class Board:
  def __init__(self, width, height, start_positions=[]):
    self.width = width
    self.height = height
    self.grid = [[0 for j in range(self.width)] for i in range(self.height)]

  def pretty_grid(self) -> str:
    formatted_grid = ('\n'.join([' '.join([str(cell) for cell in row]) for row in self.grid]))
    return formatted_grid