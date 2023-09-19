import random
import time

from lottery import util


# This lottery works by drawing the winning numbers for the current and following 3 weeks
def lottery(seed=int(time.time())):
    # Ensure we behave as if no entropy source was present
    random.seed(seed)
    print(f"Setting seed to {seed} (current timestamp)")

    draws = 4

    for i in range(draws):
        numbers = util.rng_list(6)

        print(f"The winning numbers are {' '.join([str(n) for n in numbers])}")


if __name__ == '__main__':
    lottery()
