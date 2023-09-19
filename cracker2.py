import random
import time

from cracking import searcher
from lottery import util


def crack_lottery(numbers: list[list[int]], start_timestamp=int(time.time()), interval=1000000):
    searcher.search(range(start_timestamp, start_timestamp - interval, -1),
                    lambda seed: cracker(seed, numbers))


def cracker(seed: int, numbers: list[list[int]]) -> bool:
    random.seed(seed)

    number_sets = [set(subset) for subset in numbers]

    for num_set in number_sets:
        if num_set != set(util.rng_list(len(num_set))):
            return False

    return True


if __name__ == '__main__':
    # Order of the numbers doesn't matter, but be sure to group them

    # This example is from timestamp 1695083134
    crack_lottery([[15, 16, 28, 31, 36, 45], [4, 7, 17, 19, 20, 44]])
