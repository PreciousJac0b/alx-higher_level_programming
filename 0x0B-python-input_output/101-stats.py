#!/usr/bin/python3


if __name__ == '__main__':
    import fileinput

    def print_dict(status, size):
        """Prints a dictionary in sorted order"""
        print("File size: {}".format(size))
        status = dict(sorted(status.items()))
        for elem in status:
            print("{}: {}".format(elem, status[elem]))
    i = 0
    file_size = 0
    status_code = {}
    for line in fileinput.input():
        if i % 10 == 0 and i != 0:
            print_dict(status_code, file_size)
        line = line.split()
        code = line[-2]
        size = line[-1]
        if not code:
            continue
        if code not in status_code:
            status_code[code] = 1
        else:
            status_code[code] += 1
        file_size += int(size)
        i += 1
    print_dict(status_code, file_size)
