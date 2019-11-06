#!/usr/bin/python

import argparse

def find_max_profit(prices):
    max = prices[1] - prices[0]
    for i in range(2, len(prices)):
        for j in range(0, i):
            if (dif := prices[i] - prices[j]) > max:
                max = dif
    return max

if __name__ == '__main__':
    # This is just some code to accept inputs from the command line
    parser = argparse.ArgumentParser(description='Find max profit from prices.')
    parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
    args = parser.parse_args()

    print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))