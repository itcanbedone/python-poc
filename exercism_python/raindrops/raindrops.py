def raindrops(number):
    sounds = []

    if (number % 3) == 0:
        sounds.append("Pling")

    if (number % 5) == 0:
        sounds.append("Plang")

    if (number % 7) == 0:
        sounds.append("Plong")

    if len(sounds):
        return "".join(sounds)

    return "{}".format(number)

