import random


def rng() -> int:
    return random.randint(1, 49)


def rng_list(num: int) -> list[int]:
    return [rng() for _ in range(6)]
