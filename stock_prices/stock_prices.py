#!/usr/bin/python

import argparse

def find_max_profit(prices):
    low = prices[0]
    max = prices[1] - low
    for p in prices[1:]:
        # Check difference of previous low against max profit
        if (diff := p - low) > max:
            max = diff
        # Check if current price is lower than previous low
        if p < low:
            low = p
    return max

if __name__ == '__main__':
    # This is just some code to accept inputs from the command line
    parser = argparse.ArgumentParser(description='Find max profit from prices.')
    parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
    args = parser.parse_args()

    print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))