#!/usr/bin/python

"""
Randomizes given arguments.
Usage: program.py [-u] [arg1, ..., argX] N
Params:
    -u              Output only unique args. If N > X reset unique counter.
    arg1, ..., argX Output these args.
    N               Output N args in random order.
"""

import sys
import random

def rand_unique(l, n):
    lc = l.copy()
    for i in range(n):
        print(lc.pop(random.randint(0, len(lc) - 1)), end=' ')
        if len(lc) == 0:
            lc = l.copy()

def rand(l, n):
    for i in range(n):
        print(random.choice(l), end=' ')

def main():
    argv = sys.argv[1:]
    n = int(argv.pop(len(argv) - 1))
    l = [x for x in argv if x.find('-') != 0]
    if '-u' in argv:
        rand_unique(l, n)
    else:
        rand(l, n)


if __name__ == "__main__":
    main()
