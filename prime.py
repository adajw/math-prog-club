import heapq, itertools

def factorisation(number):
    """Returns a list of the prime factors of a number in ascending order."""
    factors = []
    while number > 1:
        for factor in range(2, number + 1):
            if number % factor == 0:
                factors.append(factor)

                # floor division needed to return an int
                # required because range() needs integer values
                number //= factor
                break
    return factors
    
def primes(limit = None):
    """ Generator yielding primes below (optional) limit."""
    if limit is None:
        return _infinite_primes()
    else:
        return itertools.takewhile(lambda x: x < limit, _infinite_primes())

def _infinite_primes():
    """A generator for infinite primes."""
    
    # priority queue of the sequences of non-primes
    # the priority queue allows us to get the "next" non-prime quickly
    nonprimes = []
 
    i = 2
    while True:
        if nonprimes and i == nonprimes[0][0]: # non-prime
            while nonprimes[0][0] == i:
                # for each sequence that generates this number,
                # have it go to the next number (simply add the prime)
                # and re-position it in the priority queue
                x = nonprimes[0]
                x[0] += x[1]
                heapq.heapreplace(nonprimes, x)
 
        else: # prime
            # insert a 2-element list into the priority queue:
            # [current multiple, prime]
            # the first element allows sorting by value of current multiple
            # we start with i^2
            heapq.heappush(nonprimes, [i*i, i])
            yield i
 
        i += 1
