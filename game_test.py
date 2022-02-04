import unittest
from game import Game

class TestGame(unittest.TestCase):
  def setUp(self):
    pass

  def tearDown(self):
    pass 

  def test_play(self):
    """Game.play() populates the self.rounds attribute with steps+1 board instances"""
    # assert self.rounds has steps + 1 elements added to it
    
    self.game = Game(5, 5,
      [ # Glider config
        [1,2],
        [2,0],[2,2],
        [3,1],[3,2]
      ])

    self.game.play(20)

    self.assertEqual(len(self.game.rounds), 21)
    
if __name__ == "__main__":
  unittest.main()