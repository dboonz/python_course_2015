import functools
import time

def deprecated(func):
    def wrapper(*args, **kwargs):
        print("Don't use " + func.__name__)
        ans = func(*args, **kwargs)
        return ans
    return wrapper

#@functools.update_wrapper(func)
def logger(func):
    # keeps the documentation as-is
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(func.__name__ + " is called with args " + str(list(args)) + " and kwargs " + str(kwargs))
        ans = func(*args, **kwargs)
        print(func.__name__ + " returned " + str(ans))
        return ans
    # keep the documentation as-is
    return wrapper

def timeit(func):
    # keeps the documentation as-is
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        t0 = time.time()
        ans = func(*args, **kwargs)
        print(func.__name__, "took", time.time()-t0, "s")
        return ans
    # keep the documentation as-is
    return wrapper





# @deprecated
#@logger
@timeit
def fact(n, nmin, fancy=False, superfancy=True):
    """ Hi1!"""
    if n < nmin:
        return 1
    else:
       return n*fact(n-1, nmin, fancy=not fancy, superfancy=fancy and superfancy)



if __name__ == '__main__':
    fact(2, 1 )
    help(fact)
