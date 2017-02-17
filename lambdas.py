#playing with lambdas


def perform(f):
    f()


def foo(*args):
    for a in args:
        print(a)

addone = lambda x: x+1

def main():
    perform(lambda: foo(1,2,3,4))
    nums = [addone(x) for x in (1,2,3,4,5,6,7,8,9,10)]
    print(",".join(str(n) for n in nums))

    names = ['abc', 'def', 'ijh', 'opr', 'blabla']
    res = ", ".join(str(x) for x in names)
    print (res)

if __name__ == "__main__":
    main()
