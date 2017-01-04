import sys


# a C like struct
class Test2:
    var1 = 10
    var2 = "hello"
    var3 = []


class Test:
    var = 10

    def __init__(self):
        print("OK")

    def foo(self):
        print("Foo!")


def main():
    t1 = Test()
    t2 = Test2
    t1.foo()
    print(t2.var1)
    print(t2.var2)
    print(t2.var3)

    tests = [Test2 for i in range(10)]

    for i in range(10):
        print(tests[i].var1)


if __name__ == "__main__":
    main()
