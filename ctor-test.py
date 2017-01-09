import sys


class integer():
    def __init__(self, i) -> int:
        if not isinstance(i, int):
            self.i = None
        else:
            self.i = i


# a C like struct but they are all like static
class Test2:
    var1 = 10
    var2 = "hello"
    var3 = []


class Test3:
    def __init__(self) -> object:
        self.var1 = 10
        self.var2 = "hello"
        self.var3 = []


class Test:
    var = 10

    def __init__(self):
        print("OK")

    def foo(self):
        print("Foo!")


def main():
    t1 = Test()
    t2 = Test3()
    t3 = Test3()
    t1.foo()
    print(t2.var1)
    print(t2.var2)
    print(t2.var3)
    t3.var1 = 10000
    tests = [Test2 for i in range(10)]

    print(t2.var1)
    print(t3.var1)

    for i in range(10):
        print(tests[i].var1)

    myint = integer(1233333)
    print(myint.i)


if __name__ == "__main__":
    main()
