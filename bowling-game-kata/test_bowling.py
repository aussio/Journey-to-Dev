import unittest
import bowling

# unittest.TestCase

class GameTest(unittest.TestCase):

    def setUp(self):
        self.dasbowling = bowling.Game()

    def roll_many(self, amount_rolls, pins):
        for x in range(amount_rolls):
            self.dasbowling.roll(pins)

    def test_guttergame(self):
        self.roll_many(20, 0)
        self.assertEqual(self.dasbowling.score(), 0)

    def test_lowball(self):
        self.roll_many(20, 1)
        self.assertEqual(self.dasbowling.score(), 20)

    def test_spare(self):
        self.dasbowling.roll(5)
        self.dasbowling.roll(5)
        self.dasbowling.roll(3)
        self.roll_many(17, 0)
        self.assertEqual(self.dasbowling.score(), 16)

    def test_strike(self):
        self.dasbowling.roll(10)
        self.roll_many(3, 3)
        self.roll_many(16, 0)
        self.assertEqual(self.dasbowling.score(), 25)
