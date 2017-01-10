"""parameters to functions some examples I noticed
    demonstrates throwing exceptions when something
    bad happens, also :)
"""

def passAList(lstref=[]):
    """I expect a list"""
    if not isinstance(lstref, list):
        raise  ValueError("Expecting a list reference: []")
    else:
        for i in lstref:
            print(i)


def passATuple(tulref=()):
    if not isinstance(tulref, tuple):
        raise ValueError("Expecting a tuple reference: ()")
    else:
        for i in tulref:
            print(i)

def passAMap(mapref={}):
    if not isinstance(mapref, dict):
        raise Exception("Expecting a dictionary: {}")
    else:
        for k, v in mapref.items():
            print(str(k)+":"+str(v))

def main():
    passAList([1,2,3,4,5,6])
    passAMap({"name":"maria", "age":10, "town":"unknown"})
if __name__ == "__main__":
    main()
