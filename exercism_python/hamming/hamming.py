def distance(strand_a, strand_b):

    if len(strand_a) != len(strand_b):
        raise ValueError("Strands are not the same size.")

    return sum(sa != sb for sa, sb in zip(strand_a, strand_b))

