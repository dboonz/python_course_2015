Decorators and Context Managers
====================

Speaker: Zbigniew Jedrezejewski-Szmek

Example:

def deprecated(func):
    def wrapper(*arg, **kwargs):#*
        print("Don't use " + func.__name__)
        ans = func(*args, **kwargs) #*
        return ans
    return wrapper

@deprecated
def fact(n):
    if n <= 1:
        return 1
    else:
       return n*fact(n-1)

Generators
====================


