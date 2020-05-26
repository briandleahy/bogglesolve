import unittest

from bogglesolve.main import solve, BOGGLE_SOLVER
from bogglesolve.board import BoggleBoard
from bogglesolve.tests import common
from bogglesolve.tests.common import GAME1, GAME2, GAME3


BOARDS = [BoggleBoard.create_from_formatted_text(game.board_text)
          for game in [GAME1, GAME2, GAME3]]


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

    def test_all_known_words_found_in_game_3(self):
        found_words = solve(GAME3.board_text)
        known_words = GAME3.words
        for word in known_words:
            self.assertIn(word, found_words)


class TestTransformationInvariant(unittest.TestCase):
    def test_invariant_to_rotation(self):
        for which, board_original in enumerate(BOARDS):
            board_transformed = common.rotate_board_90_degrees(board_original)
            text_transformed = board_transformed.transform_to_formatted_text()
            words_transformed = solve(text_transformed)

            text_original = board_original.transform_to_formatted_text()
            words_original = solve(text_original)

            with self.subTest(game=which):
                self.assertEqual(words_original, words_transformed)

    def test_invariant_to_flipping_leftright(self):
        for which, board_original in enumerate(BOARDS):
            board_transformed = common.flip_board_leftright(board_original)
            text_transformed = board_transformed.transform_to_formatted_text()
            words_transformed = solve(text_transformed)

            text_original = board_original.transform_to_formatted_text()
            words_original = solve(text_original)

            with self.subTest(game=which):
                self.assertEqual(words_original, words_transformed)

    def test_invariant_to_flipping_updown(self):
        for which, board_original in enumerate(BOARDS):
            board_transformed = common.flip_board_updown(board_original)
            text_transformed = board_transformed.transform_to_formatted_text()
            words_transformed = solve(text_transformed)

            text_original = board_original.transform_to_formatted_text()
            words_original = solve(text_original)

            with self.subTest(game=which):
                self.assertEqual(words_original, words_transformed)

    def test_invariant_to_flipping_and_rotation(self):
        for which, board_original in enumerate(BOARDS):
            board_transformed = common.flip_board_updown(
                common.rotate_board_90_degrees(board_original))
            text_transformed = board_transformed.transform_to_formatted_text()
            words_transformed = solve(text_transformed)

            text_original = board_original.transform_to_formatted_text()
            words_original = solve(text_original)

            with self.subTest(game=which):
                self.assertEqual(words_original, words_transformed)



if __name__ == '__main__':
    unittest.main()
