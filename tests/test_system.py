import unittest

from bogglesolve.main import solve, BOGGLE_SOLVER
from bogglesolve.tests.common import GAME1, GAME2


class TestRealBoards(unittest.TestCase):
    def test_returns_same_result_for_capitalized(self):
        found_lower = solve(GAME1.board_text.lower())
        found_upper = solve(GAME1.board_text.upper())
        self.assertEqual(found_lower, found_upper)

    def test_all_found_words_in_dictionary_for_game_1(self):
        found_words = solve(GAME1.board_text)
        for word in found_words:
            self.assertIn(word, BOGGLE_SOLVER.valid_words)

    def test_all_known_words_found_in_game_1(self):
        found_words = solve(GAME1.board_text)
        known_words = GAME1.words
        for word in known_words:
            self.assertIn(word, found_words)

    def test_no_duplicates_for_game1(self):
        found_words = solve(GAME1.board_text)
        for word in found_words:
            self.assertEqual(found_words.count(word), 1)

    def test_all_found_words_in_dictionary_for_game_2(self):
        found_words = solve(GAME2.board_text)
        for word in found_words:
            self.assertIn(word, BOGGLE_SOLVER.valid_words)

    def test_all_known_words_found_in_game_2(self):
        found_words = solve(GAME2.board_text)
        known_words = GAME2.words
        for word in known_words:
            self.assertIn(word, found_words)

    def test_no_duplicates_for_game2(self):
        found_words = solve(GAME2.board_text)
        for word in found_words:
            self.assertEqual(found_words.count(word), 1)


if __name__ == '__main__':
    unittest.main()
