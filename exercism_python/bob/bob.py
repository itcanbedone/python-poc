import re

def count_lowercase(phrase):
    return sum(1 for char in phrase if char.islower())

def count_uppercase(phrase):
    return sum(1 for char in phrase if char.isupper())

def is_a_question(phrase):
    result = 0

    if re.search(r'[?]$', phrase.rstrip()):
        result = 1

    return result

def hey(phrase):

    if not phrase or phrase.isspace():
        result = "Fine. Be that way!"

    elif count_lowercase(phrase) < 1 < count_uppercase(phrase):
        if is_a_question(phrase):
            result = "Calm down, I know what I'm doing!"
        else:
            result = "Whoa, chill out!"

    elif is_a_question(phrase):
        result = "Sure."

    else:
        result = "Whatever."

    return result
