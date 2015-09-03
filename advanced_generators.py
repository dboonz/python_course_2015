import functools


def lucky_numbers(n):
    ans = []
    for i in range(n):
        if i % 7 != 0:
            continue
        if sum(int(digit) for digit in str(i)) % 3 != 0:
            continue
        ans.append(i)
    return ans

def listize(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        return_list = []
        for l in func(*args, **kwargs):
            return_list.append(l)
        return return_list
    return wrapper


@listize
def lucky_numbers_generator(n):
    for i in range(n):
        if i % 7 != 0:
            continue
        if sum(int(digit) for digit in str(i)) % 3 != 0:
            continue
        yield i






if __name__ == '__main__':
    ln = lucky_numbers(100)
    lng = lucky_numbers_generator(100)
    lng = lucky_numbers_generator(100)
    print(lng)
    print(ln)
    for l in lng:
        print(l)

