class Board:
  def __init__(self, width=5, height=5, positions=[]):
    self.width = width
    self.height = height
    self.grid = [[0 for j in range(self.width)] for i in range(self.height)]
    self.populate(positions)

  def pretty_grid(self):
    """A method that returns a formatted string of self.grid"""
    formatted_grid = ('\n'.join([' '.join([str(cell) for cell in row]) for row in self.grid]))
    return formatted_grid

  def populate(self, positions):
    """A setter method that populates self.grid with ones at specified 2D indices"""
    for index_set in positions:
      i, j = index_set
      self.grid[i][j] = 1
  
  