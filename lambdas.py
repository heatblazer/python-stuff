#playing with lambdas


def perform(f):
    f()


def foo():
    print("foo!\n")


def main():
    perform(lambda: foo())

if __name__ == "__main__":
    main()
