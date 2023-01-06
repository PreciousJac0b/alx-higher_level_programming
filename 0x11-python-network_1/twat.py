#!/usr/bin/python3

from urllib.request import urlopen
from pprint import pprint
with urlopen("https://www.isitchristmas.com") as response:
    pprint(dir(response))
