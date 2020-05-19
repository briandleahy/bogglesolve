"""Stores some pairs of boards with known words in them, found by playing
two games of Boggle :)"""

from collections import namedtuple


AnswerKey = namedtuple('AnswerKey', ('board', 'words'))


GAME1 = AnswerKey(
    board=(
        "cenu\n" +
        "pien\n" +
        "hgda\n" +
        "bttn"
    ),
    words={
        'tan',
        'ant',
        'tad',
        'gin',
        'pig',
        'gip',
        'dip',
        'pie',
        'hip',
        'hide',
        'nice',
        'ice',
        'pine',
        'pined',
        'die',
        'dine',
        'din',
        'pin',
        'nip',
        'need',
        'dean',
        'eat',
        'neat',
        'neg',
        'pee',
        'gee',
        'and',
        'dice',
        'dean',
        'ane',
        'att',
        'cig',
        'dan',
        'eide',
        'end',
        'ged',
        'gen',
        'gid',
        'gie',
        'gied',
        'gien',
        'hid',
        'idea',
        'nae',
        'nan',
        'neat',
        'pied',
        'tae',
        'unde',
    }
)

GAME2 = AnswerKey(
    board=(
        'damh\n' +
        'letg\n' +
        'bnoc\n' +
        'dafh'
    ),
    words={
        'nab',
        'ban',
        'bane',
        'dam',
        'deal',
        'lead',
        'laden',
        'lent',
        'net',
        'ten',
        'mend',
        'end',
        'dame',
        'tame',
        'tea',
        'den',
        'dent',
        'team',
        'not',
        'note',
        'ton',
        'tone',
        'toned',
        'bent',
        'beam',
        'met',
        'toad',
        'let',
        'teal',
        'male',
        'toe',
        'fan',
        'neat',
        'meat',
        'noel',
        'cot',
        'fad',
        'and',
        'band',
        'ant',
        'font',
        'meal',
        'goth',
        'death',
        'blend',
        'fable',
        'able',
    },
)

