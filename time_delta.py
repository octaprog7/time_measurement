#!/usr/bin/env python3
import time
# import datetime
from sys import version_info
"""
Time interval measurement tools.
Python version 3.7+!
"""

assert version_info >= (3, 7)


def get_time_ns() -> int:
    """return time in nanosecond. versio 1"""
    return time.process_time_ns()


def get_time_nsec() -> int:
    """return time in nanosecond. versio 2"""
    return time.time_ns()


class TimeDelta:
    """time interval measurement"""

    def __init__(self, gettimefunc=get_time_ns):
        self.timefunc = gettimefunc
        self.start = self.timefunc()

    def start(self):
        """call start before measurement"""
        self.__init__()

    def stop(self):
        """return delta time in nanosecond"""
        return self.timefunc() - self.start


if "__main__" == __name__:
    N = 1_000
    funcs = get_time_ns, get_time_nsec
    for func in funcs:
        TD = TimeDelta(func)
        for i in range(N):
            print(i, end=' ')
        print("\n")
        #
        print(f"Execution time of {N} iterations of the loop in nanoseconds: {TD.stop()}")
