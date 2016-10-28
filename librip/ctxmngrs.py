import time

class timer:
    def __enter__(self):
        self.start = time.clock()
    def __exit__(self, exp_type, exp_value, traceback):
        print(time.clock() - self.start)
