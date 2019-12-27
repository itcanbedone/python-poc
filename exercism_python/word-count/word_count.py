import re

def word_count(phrase):
    words = {}

    for word in re.findall(r"(?<![@#])[^\W_]+(?:'[^\W_]+)?", phrase.lower()):
        if word in words:
            words[word] += 1
        else:
            words[word] = 1

    return words


