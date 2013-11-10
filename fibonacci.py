import math, itertools

def _fibonacci():
    """ Underlying generator implementation. """
    yield 1
    f1 = 1
    f2 = 1
    while True:
        yield f2
        f1, f2 = f2, f1 + f2   

def fibonacci(limit=None):
    """ A generator for the fibonacci sequence, accepting a limit and a condition.

        limit (optional) is a number that the sequence will not exceed.
    """
    if limit is None:
        return _fibonacci()  
    else:
        return itertools.takewhile(lambda x: x < limit, _fibonacci())

def nth_fibonacci(n):
    if n >= 72:
        print("WARNING: nth_fibonacci not accurate beyond n = 72")
    phi = (1 + math.sqrt(5))/2
    q = (1 - math.sqrt(5))/2
    return math.floor((math.pow(phi, n) - math.pow(q, n)) / math.sqrt(5))

