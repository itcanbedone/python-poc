import re
import collections
#from collections import Counter

def is_isogram(word):
    lc_word = re.sub(r"\W", '', word.lower())
    my_set = set(lc_word)
    print(lc_word)
    print(len(my_set))

    return True
#    return len(lc_word) == len(collections.Counter(lc_word))
#    lc_word = re.sub(r"\W", '', word.lower())
#    c = collections.Counter(lc_word).most_common()
#    c = collections.Counter(lc_word)

#    if len(lc_word) != len(list(c)):
#        return False
#    print(lc_word)
#    print(len(lc_word))
#    print(len(list(c)))
#    for c in range(len(lc_word)):
#        print(lc_word)
#        print(c)
#        print(lc_word.rfind(lc_word[c]))
#        if lc_word.rfind(lc_word[c]) != c:
#            return False
#    return True

if __name__ == '__main__':
    is_isogram('isogram')
    is_isogram('isograms')
    is_isogram('subdermatoglyphic')
    is_isogram('sub-derma-toglyphic')
