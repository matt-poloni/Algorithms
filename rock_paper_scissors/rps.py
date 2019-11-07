#!/usr/bin/python

import sys

def rock_paper_scissors(n):
    rps=['rock', 'paper', 'scissors']
    result = []
    def loop(num, list=None):
        # Initialize a list if none was given (top call only)
        if list == None:
            list = []
        # If you've generated all plays, add series to results
        if num == 0:
            nonlocal result
            result.append(list)
        # Otherwise, loop through each play and feed to next recursion
        else:
            for play in rps:
                loop(num - 1, [*list, play])
    loop(n) # Start the recursion
    return result

if __name__ == "__main__":
    if len(sys.argv) > 1:
        num_plays = int(sys.argv[1])
        print(rock_paper_scissors(num_plays))
    else:
        print('Usage: rps.py [num_plays]')