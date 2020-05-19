from collections import deque, namedtuple

from bogglesolve.board import TextPath


class BoggleSolver(object):
    def __init__(self, valid_words):
        self.valid_words = set(valid_words)
        self.valid_prefixes = self._setup_valid_prefixes()

    def solve(self, boggle_board):
        queue = self.initialize_queue(boggle_board)
        found_words = deque()
        while len(queue) > 0:
            path = queue.pop()
            path_properties = self.query_path_properties(path)
            if path_properties.is_valid_word:
                found_words.append(path)
            if path_properties.is_valid_prefix:
                additional_paths = path.branch()
                queue.extendleft(additional_paths)
        return found_words

    def query_path_properties(self, path):
        is_valid_word = path.text in self.valid_words
        is_valid_prefix = path.text in self.valid_prefixes
        return PathProperty(is_valid_word, is_valid_prefix)

    def initialize_queue(self, boggle_board):
        queue = [
            TextPath(boggle_board, ((i, j),))
            for i in range(boggle_board.shape[0])
            for j in range(boggle_board.shape[1])]
        return deque(queue)

    def _setup_valid_prefixes(self):
        valid_prefixes = set()
        maxlength = max([len(w) for w in self.valid_words])
        # since this is just prefixes, we only need to go up to the
        # length of the longest word minus 1
        for length in range(1, maxlength):
            prefixes_length_l = [w[:length] for w in self.valid_words]
            valid_prefixes.update(prefixes_length_l)
        return valid_prefixes


PathProperty = namedtuple('PathProperty', ('is_valid_word', 'is_valid_prefix'))

