#!/usr/bin/python
import time
  
class TimeDelta:
    def __init__(self):
        self.start = time.process_time_ns()
        self.delta = 0
    def start(self):
        self.__init__(self)
    def stop(self):
        self.delta = time.process_time_ns() - self.start
        return self.delta
    # return delta time is second
    def get_delta(self):
        return self.delta / 1000000000.0


if __name__ == "__main__":
    # assigning n = 50  
    n = 50 
    # Start the stopwatch / counter  
    TD = TimeDelta()
    for i in range(n): 
        print(i, end =' ') 
    TD.stop()
    #
    print("Elapsed time during the whole program in nanoseconds:", TD.get_delta())

