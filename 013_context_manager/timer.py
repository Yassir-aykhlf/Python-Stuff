"""This module provides a context manager class that measures the time
taken to execute a block of code and prints the result upon exit.
"""

import time

class Timer:
    """measures the time taken to execute a block of code and prints the result upon exit."""
    def __init__(self) -> None:
        self._start: float = 0
        self._end: float = 0

    def __enter__(self):
        self._start = time.perf_counter()

    def __exit__(self, _exc_type: type[BaseException] | None,
                 _exc_value: BaseException | None,
                 _exc_tb: object | None) -> None:
        self._end = time.perf_counter()
        print(f"{self._end - self._start:.6f} seconds")

if __name__ == "__main__":
    with Timer():
        total: int = 0
        for i in range(1_000_000):
            total += i
    print(total)
