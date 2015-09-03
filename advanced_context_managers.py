from contextlib import contextmanager
import time
# the context manager is a nice way to time execution for functions that are not easily decorated

# hard way:

class logtime:
    def __enter__(self):
        # setup here
        pass
    def __exit__(self):
        # destroy here
        pass

# easy way
@contextmanager
def logtime_cm():
    t0 = time.time()
    yield
    t1 = time.time()
    print("Execution took %.5f ms" % (1000*(t1-t0)))


def taketime(t):
    time.sleep(t)

if __name__ == '__main__':

    with logtime_cm():
        time.sleep(0.4)



