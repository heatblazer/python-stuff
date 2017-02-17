import pyqtgraph as pg
import os
import sys


def cmpfoo(a, b):
    if a > b:
        return False
    else:
        return True


def main(*args):
    a = [2, 4, 55, 1, 2, 4, 5]
    a.sort(cmp=cmpfoo)

if __name__ == "__main__":
    main(sys.argv)
