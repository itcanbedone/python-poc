import re

def abbreviate(words):
    acronym = []

    for word in re.findall(r"(?:^| |-)([a-zA-Z])", words):
        acronym.append(word[0])

    return ''.join(acronym).upper()


