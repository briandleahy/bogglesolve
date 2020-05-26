import unittest

from bogglesolve.board import BoggleBoard
from bogglesolve.tests import common


_chars = (
    ('a', 'b', 'c', 'd'),
    ('e', 'f', 'g', 'h'),
    ('i', 'j', 'k', 'l'),
    ('m', 'n', 'o', 'p'),
)

BOARD = BoggleBoard(_chars)

class TestTransformBoards(unittest.TestCase):
    def test_rotate_board_90_degrees(self):
        rotated = common.rotate_board_90_degrees(BOARD)
        correct = (
            ('a', 'e', 'i', 'm'),
            ('b', 'f', 'j', 'n'),
            ('c', 'g', 'k', 'o'),
            ('d', 'h', 'l', 'p'),
        )
        self.assertEqual(rotated.characters, correct)

    def test_flip_board_leftright(self):
        flipped = common.flip_board_leftright(BOARD)
        correct = (
            ('d', 'c', 'b', 'a'),
            ('h', 'g', 'f', 'e'),
            ('l', 'k', 'j', 'i'),
            ('p', 'o', 'n', 'm'),
        )
        self.assertEqual(flipped.characters, correct)

    def test_flip_board_updown(self):
        flipped = common.flip_board_updown(BOARD)
        correct = (
            ('m', 'n', 'o', 'p'),
            ('i', 'j', 'k', 'l'),
            ('e', 'f', 'g', 'h'),
            ('a', 'b', 'c', 'd'),
        )
        self.assertEqual(flipped.characters, correct)


if __name__ == '__main__':
    unittest.main()

