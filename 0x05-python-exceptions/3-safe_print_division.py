#!/usr/bin/python3


def safe_print_division(a, b):
    value = 0
    try:
        value = a / b
    except (ValueError, ZeroDivisionError):
        return None
    finally:
        print("Inside result: {}".format(value))
        return value
