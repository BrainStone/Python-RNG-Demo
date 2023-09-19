import random
import time

from cracking import searcher
from lottery import util


def crack_lottery(numbers: list[int], start_timestamp=int(time.time()), interval=1000000):
    searcher.search(range(start_timestamp, start_timestamp - interval, -1),
                    lambda seed: cracker(seed, numbers))


def cracker(seed: int, numbers: list[int]) -> bool:
    random.seed(seed)

    for num in numbers:
        if num != util.rng():
            return False

    return True


if __name__ == '__main__':
    # Specify the numbers here. Order matters! If they are unordered or sorted, use demo2

    # This example is from timestamp 1695080643
    crack_lottery([23, 7, 24, 2, 8, 29, 31, 28, 28, 42, 29, 10])
