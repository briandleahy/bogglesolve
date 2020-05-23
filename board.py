import itertools


class BoggleBoard(object):
    def __init__(self, characters):
        """
        Parameters
        ----------
        character : nested tuples
            For standard boggle, a 4-tuple, with each element a 4-tuple of
            strings
        """
        self.characters = characters
        rows = len(self.characters)
        cols = len(self.characters[0])
        if not all([len(c) == cols for c in self.characters]):
            raise ValueError("Invalid input characters")
        self.shape = (rows, cols)

    @classmethod
    def create_from_formatted_text(cls, text):
        text = text.lower()
        rows = [l for l in text.split('\n') if len(l) > 0]
        characters = tuple([cls._format_text_row(row) for row in rows])
        return cls(characters)

    @classmethod
    def _format_text_row(cls, row):
        if 'qu' in row:
            sections = row.split('qu')
            out = tuple()
            for section in sections[:-1]:
                out = out + tuple(section) + ('qu',)
            out = out + tuple(sections[-1])
        else:
            out = tuple(row)
        return out


class TextPath(object):
    def __init__(self, boggle_board, path_indices):
        """
        boggle_board : BoggleBoard
        path_indices : (N, 2) element tuple-like of indices
        """
        if not all([len(p) == 2 for p in path_indices]):
            raise ValueError("`path_indices` must be an (N, 2) element tuple")
        self.boggle_board = boggle_board
        self.path_indices = tuple(path_indices)

    @property
    def text(self):
        chars = [self.boggle_board.characters[i][j]
                 for i, j in self.path_indices]
        return ''.join(chars)

    def branch(self):
        current_points = self.path_indices
        last_index = current_points[-1]
        board_shape = self.boggle_board.shape
        branched_paths = list()

        for di, dj in itertools.product([-1, 0, 1], [-1, 0, 1]):
            next_point = (last_index[0] + di, last_index[1] + dj)
            not_used_twice = (next_point not in current_points)
            point_in_board = (
                all([next_point[i] < board_shape[i] for i in [0, 1]])
                and
                all([next_point[i] >= 0 for i in [0, 1]]))
            if not_used_twice and point_in_board:
                new_path = current_points + (next_point,)
                branched_paths.append(new_path)
        return [TextPath(self.boggle_board, path) for path in branched_paths]

