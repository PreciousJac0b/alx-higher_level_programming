#!/usr/bin/python3
import sys


def main():
    n = len(sys.argv)
    if n == 1:
        print("0 arguments.")
    elif n == 2:
        print("{} argument:".format(1))
        print("1: {}".format(sys.argv[1]))
    else:
        print("{} arguments:".format(n - 1))
        for i in range(1, n):
            print("{}: {}".format(i, sys.argv[i]))


if __name__ == "__main__":
    main()
