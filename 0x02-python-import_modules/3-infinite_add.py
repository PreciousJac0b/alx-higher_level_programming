#!/usr/bin/python3
import sys


def main():
    n = len(sys.argv)
    result = 0

    for i in range(1, n):
        result += int(sys.argv[i])

    print("{}".format(result))


if __name__ == "__main__":
    main()
