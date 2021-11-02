#!/usr/bin/env python3
import time
from sys import version_info
"""
Time interval measurement tools.
Python version 3.7+!
"""

assert version_info >= (3, 7)


class TimeDelta:
    """time interval measurement"""

    @staticmethod
    def get_time() -> int:
        """return time in nanosecond"""
        return time.process_time_ns()

    def __init__(self):
        self.start = TimeDelta.get_time()

    def start(self):
        """call start before measurement"""
        self.__init__()

    def stop(self) -> int:
        """return delta time in nanosecond"""
        return TimeDelta.get_time() - self.start


if "__main__" == __name__:
    N = 1_000_000
    TD = TimeDelta()
    for i in range(N):
        print(i, end=' ')
    print("\n")
    #
    print(f"Execution time of {N} iterations of the loop in nanoseconds: {TD.stop()}")
