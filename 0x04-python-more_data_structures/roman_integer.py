#!/usr/bin/python3


def roman_integer(s):
    roman_dict =  {
            "I": 1,
            "V": 5,
           "X": 10,
           "L" : 50,
           "C" : 100,
            "D": 500,
            "M": 1000,
            }
    counter = 0
    i = 0
    # MCMXCIV
    """
    1000 - 100 + 1000 - 10 + 100 - I 
    s[0] => M
    roman_dict[M}
    MCMXCIV => 7
    s = 6
    s[6] = v
    s[6] < s[7] => S[7] str index out of range.
    s[5] < s[6]
    """
    while i <= (len(s) - 2):
        if roman_dict[s[i]] < roman_dict[s[i + 1]]:
            counter -= roman_dict[s[i]]
            print("counter is {} -> {}".format(counter, roman_dict[s[i]]))
        else:
            counter += roman_dict[s[i]]
            print("counter is {}, {}".format(counter, roman_dict[s[i]]))
        i += 1
    counter += roman_dict[s[-1]]
    return counter



print(roman_integer("MCMXCIV"))
print(roman_integer("LVIII"))
print(roman_integer("III"))


