"""
TWL06 Scrabble Word List, downloaded from
https://www.wordgamedictionary.com/twl06/download/twl06.txt
"""

from bogglesolve.util import read_words


def make_boggle_words():
    scrabble_words = read_words('scrabble-words.txt')
    boggle_words = [w for w in scrabble_words if len(w) >= 3]

    boggle_to_save = '\n'.join(sorted(boggle_words)) + '\n'
    with open('boggle-words.txt', 'w') as f:
        f.write(boggle_to_save)


if __name__ == '__main__':
    make_boggle_words()

