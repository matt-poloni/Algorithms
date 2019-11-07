#!/usr/bin/python

import sys

# The cache parameter is here for if you want to implement
# a solution that is more efficient than the naive 
# recursive solution
def factorial(n, cache=[]):
    # Try to return a cached value
    try:
        result = cache[n]
    # If a cached value doesn't exist...
    except:
        if len(cache) == 0:
            cache.extend([1, 1])
        # Generate new factorials from the largest cached
        for i in range(len(cache), n+1):
            # And cache each new factorial along the way
            cache.append(i * cache[i-1])
        result = cache[n]
    return result

def eating_cookies(n, cache={}):
    try:
        return cache[n]
    except:
        if n < 0:
            print("ERROR: No negative numbers allowed")
        elif n < 4:
            cache[0] = 1
            cache[1] = 1
            cache[2] = 2
            cache[3] = 4
    return cache[n]
        
        
    

if __name__ == "__main__":
    if len(sys.argv) > 1:
        num_cookies = int(sys.argv[1])
        print("There are {ways} ways for Cookie Monster to eat {n} cookies.".format(ways=eating_cookies(num_cookies), n=num_cookies))
    else:
        print('Usage: eating_cookies.py [num_cookies]')