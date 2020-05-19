import unittest

from bogglesolve.bogglesolve import BoggleSolver
from bogglesolve.board import BoggleBoard, TextPath


class TestBoggleSolve(unittest.TestCase):
    def test_solve_does_not_find_words_that_are_not_present(self):
        ham_solver = BoggleSolver({'ham'})  # the only valid word is "ham"
        does_not_contain_ham = (
            "xxhx\n" +
            "axxx\n" +
            "xxxx\n" +
            "xxxm"
        )
        # the board does not contain `ham`, but it does contain the
        # individual characters
        board = BoggleBoard.create_from_formatted_text(does_not_contain_ham)
        words = ham_solver.solve(board)
        self.assertEqual(len(words), 0)

    def test_solve_works_with_qu(self):
        quite_solver = BoggleSolver({'quite'})  # the only valid word is "quite"
        contains_quite_characters = (
            ("qu", "i", "t", "e"),
            ("x",  "x", "x", "x"),
            ("x",  "x", "x", "x"),
            ("x",  "x", "x", "x"),
        )
        board = BoggleBoard(contains_quite_characters)
        words = quite_solver.solve(board)
        self.assertEqual(len(words), 1)
        self.assertEqual(words[0].text, 'quite')

    def test_solve_returns_text_paths(self):
        line_solver = BoggleSolver({'line'})  # the only valid word is "line"
        many_lines = (
            "line\n" +
            "line\n" +
            "line\n" +
            "line"
        )
        board = BoggleBoard.create_from_formatted_text(many_lines)
        words = line_solver.solve(board)
        self.assertGreater(len(words), 1)
        for word in words:
            self.assertIsInstance(word, TextPath)

    def test_initialize_queue_returns_16_objects(self):
        solver = BoggleSolver({'word'})
        text = (
            "xxxx\n" +
            "xxxx\n" +
            "xxxx\n" +
            "xxxx"
        )
        board = BoggleBoard.create_from_formatted_text(text)
        initial_queue = solver.initialize_queue(board)
        self.assertEqual(len(initial_queue), 16)

    def test_query_path_properties(self):
        solver = BoggleSolver({'xxx', 'xxxx'})
        text = (
            "xxxx\n" +
            "xxxx\n" +
            "xxxx\n" +
            "xxxx"
        )
        board = BoggleBoard.create_from_formatted_text(text)
        path = TextPath(board, ((0, 0), (1, 1), (2, 2)))
        assert 'xxx' == path.text
        # now path.text is both a valid prefix and a valid word

        query_result = solver.query_path_properties(path)
        self.assertTrue(query_result.is_valid_prefix)
        self.assertTrue(query_result.is_valid_word)

    def test_setup_valid_prefixes(self):
        solver = BoggleSolver({'abcd'})
        valid_prefixes = {'a', 'ab', 'abc'}
        self.assertEqual(solver.valid_prefixes, valid_prefixes)


if __name__ == '__main__':
    unittest.main()
