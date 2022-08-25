#!/usr/bin/python3
import hidden_4


def main():
    lists = dir(hidden_4)
    for i in range(len(lists)):
        if lists[i][:2] != '__':
            print("{}".format(lists[i]))


if __name__ == '__main__':
    main()
