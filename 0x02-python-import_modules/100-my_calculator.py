#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
import sys


def main():
    argv = sys.argv
    if len(argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    else:
        one = argv[1]
        two = argv[2]
        three = argv[3]
        if argv[2] not in '+*-/':
            print("Unknown operator. Available operators: +, -, * and /")
            exit(1)
        elif argv[2] == '-':
            subbed = sub(int(one), int(three))
            print("{} {} {} = {}".format(one, two, three, subbed))
        elif argv[2] == '+':
            added = add(int(one), int(three))
            print("{} {} {} = {}".format(one, two, three, added))
        elif argv[2] == '*':
            multi = mul(int(one), int(three))
            print("{} {} {} = {}".format(one, two, three, multi))
        elif argv[2] == '/':
            divi = div(int(one), int(three))
            print("{} {} {} = {}".format(one, two, three, divi))


if __name__ == '__main__':
    main()
