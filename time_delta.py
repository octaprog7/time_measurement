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
    N = 50 
    TD = TimeDelta()
    for i in range(N): 
        print(i, end =' ') 
    TD.stop()
    #
    print("Elapsed time during the whole program in seconds:", TD.get_delta())

