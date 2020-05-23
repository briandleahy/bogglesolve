import unittest

from bogglesolve.board import BoggleBoard, TextPath


class TestBoggleBoard(unittest.TestCase):
    def test_init_raises_error_if_board_not_rectangular(self):
        incorrect_input = (
            ('a', 'b', 'c', 'd'),
            ('a', 'b', 'c', 'd'),
            ('a', 'b', 'c'),
            ('a', 'b', 'c', 'd')
        )
        self.assertRaises(ValueError, BoggleBoard, incorrect_input)

    def test_init_handles_qu(self):
        characters = (
            ('a', 'b', 'c', 'd'),
            ('a', 'b', 'c', 'd'),
            ('qu', 'r', 's', 't'),
            ('a', 'b', 'c', 'd')
        )
        board = BoggleBoard(characters)
        self.assertEqual(board.characters, characters)

    def test_create_from_formatted_text_without_qu(self):
        text = (
            'abcd\n' +
            'efgh\n' +
            'ijkl\n' +
            'mnop'
        )
        characters = (
            ('a', 'b', 'c', 'd'),
            ('e', 'f', 'g', 'h'),
            ('i', 'j', 'k', 'l'),
            ('m', 'n', 'o', 'p'),
        )
        board = BoggleBoard.create_from_formatted_text(text)
        self.assertEqual(board.characters, characters)

    def test_create_from_formatted_text_with_qu(self):
        text = (
            'abcd\n' +
            'efgh\n' +
            'ijkqu\n' +
            'mnop'
        )
        characters = (
            ('a', 'b', 'c', 'd'),
            ('e', 'f', 'g', 'h'),
            ('i', 'j', 'k', 'qu'),
            ('m', 'n', 'o', 'p'),
        )
        board = BoggleBoard.create_from_formatted_text(text)
        self.assertEqual(board.characters, characters)

    def test_format_text_row_with_qu(self):
        row = 'abquc'
        out = BoggleBoard._format_text_row(row)
        correct = ('a', 'b', 'qu', 'c')
        self.assertEqual(out, correct)

    def test_format_text_row_without_qu(self):
        row = 'abcd'
        out = BoggleBoard._format_text_row(row)
        correct = ('a', 'b', 'c', 'd')
        self.assertEqual(out, correct)


if __name__ == '__main__':
    unittest.main()

