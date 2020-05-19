

def read_words(filename):
    with open(filename) as f:
        contents = f.read()
    words = [w for w in contents.split('\n') if len(w) > 0 and ' ' not in w]
    return set(words)

