"""experimenting with out of scope objects and destrution"""

class A():

    def __init__(self):
        print("A()")

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("exit A")

    def __del__(self):
        print("~A()")


def main():
    if True:
        a = A()
    
    print("Exiting main...")

if __name__ == "__main__":
    main()

