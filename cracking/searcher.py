from typing import Callable, Collection

import alive_progress


def search(timestamp_range: Collection[int], search_func: Callable[[int], bool]) -> list[int]:
    size = len(timestamp_range)
    matches: list[int] = []

    with alive_progress.alive_bar(size) as bar:
        for timestamp in timestamp_range:
            if search_func(timestamp):
                print(f"Found match at {timestamp}")
                matches.append(timestamp)

            bar()

    return matches
