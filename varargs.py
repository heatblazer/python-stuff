

def argstest(*args, **kargs):
    for arg in args:
        print(arg)

    for key, val in kargs.items():
        print(str(key)+":"+str(val))


def main():
    argstest(1, 2, 3, 4, 5, 6, 7, name="somebody", age=1000, location="somwhere")


if __name__ == "__main__":
    main()
