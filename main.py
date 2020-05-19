import os

from bogglesolve.util import read_words
from bogglesolve.board import BoggleBoard
from bogglesolve.bogglesolve import BoggleSolver


def make_default_boggle_solver():
    loadfilename = os.path.join(
        os.path.dirname(os.path.abspath(__file__)),
        'boggle-words.txt')
    words = read_words(loadfilename)
    return BoggleSolver(words)


BOGGLE_SOLVER = make_default_boggle_solver()


def main():
    print("Please input boggle board")
    rows = list()
    for _ in range(4):
        rows = rows + input()
    return solve(rows)


def solve(rows):
    board = BoggleBoard.create_from_formatted_text(rows)
    paths = BOGGLE_SOLVER.solve(board)
    words = [path.text for path in paths]
    return sorted(set(words))

