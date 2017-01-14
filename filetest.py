import sys


def main(args=()):
    for a in args:
        print(args)
    #C like 'a' append, 'w' write, also creates it... obviously
    with open("test.txt", "a") as f:
        f.write("some data\n\n")

if __name__ == '__main__':
    main(sys.argv)
