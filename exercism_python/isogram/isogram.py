import re

def is_isogram(word):
   lc_word = re.sub(r"\W", '', word.lower())
   return len(lc_word) == len(set(lc_word))
