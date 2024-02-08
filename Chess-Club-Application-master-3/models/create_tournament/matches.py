from itertools import combinations
import random


def generate_pairings(players):
    pairings = list(combinations(players, 2))
    random.shuffle(pairings)
    return pairings
