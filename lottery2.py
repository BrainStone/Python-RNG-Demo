import random
import time

from lottery import util


# Same as demo1, but this time the numbers are sorted!
def lottery(seed=int(time.time())):
    # Ensure we behave as if no entropy source was present
    random.seed(seed)
    print(f"Setting seed to {seed} (current timestamp)")

    draws = 4

    for i in range(draws):
        numbers = sorted(util.rng_list(6))

        print(f"The winning numbers are {' '.join([str(n) for n in numbers])}")


if __name__ == '__main__':
    lottery()
