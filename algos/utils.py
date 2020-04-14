import random


def random_array(size=100, lower=1, upper=100):
    return [random.randint(lower, upper) for _ in range(size)]
