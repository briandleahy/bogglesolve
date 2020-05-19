import unittest

from bogglesolve.main import solve, BOGGLE_SOLVER
from bogglesolve.tests.common import GAME1, GAME2


class TestRealBoards(unittest.TestCase):
    def test_all_found_words_in_dictionary_for_game_1(self):
        rows = tuple([tuple(row) for row in GAME1.board.split('\n')])
        found_words = solve(rows)
        for word in found_words:
            self.assertIn(word, BOGGLE_SOLVER.valid_words)

    def test_all_known_words_found_in_game_1(self):
        rows = tuple([tuple(row) for row in GAME1.board.split('\n')])
        found_words = set(solve(rows))
        known_words = GAME1.words
        for word in known_words:
            self.assertIn(word, found_words)

    def test_no_duplicates_for_game1(self):
        rows = tuple([tuple(row) for row in GAME1.board.split('\n')])
        found_words = solve(rows)
        for word in found_words:
            self.assertEqual(found_words.count(word), 1)

    def test_all_found_words_in_dictionary_for_game_2(self):
        rows = tuple([tuple(row) for row in GAME2.board.split('\n')])
        found_words = solve(rows)
        for word in found_words:
            self.assertIn(word, BOGGLE_SOLVER.valid_words)

    def test_all_known_words_found_in_game_2(self):
        rows = tuple([tuple(row) for row in GAME2.board.split('\n')])
        found_words = set(solve(rows))
        known_words = GAME2.words
        for word in known_words:
            self.assertIn(word, found_words)

    def test_no_duplicates_for_game2(self):
        rows = tuple([tuple(row) for row in GAME2.board.split('\n')])
        found_words = solve(rows)
        for word in found_words:
            self.assertEqual(found_words.count(word), 1)


if __name__ == '__main__':
    unittest.main()
