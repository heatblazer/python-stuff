from xmlrpc.server import SimpleXMLRPCServer


class rpcserver:
    """
    simple rpc server takes (host and port) args then registers
    a function
    """
    def __init__(self, host, port):
        self.m_server = SimpleXMLRPCServer((host, port))
        print("Listen to"+str(host)+":"+str(port))


def say_moo():
    print("Mooo!\n")


r = rpcserver("localhost", 8000)
r.m_server.register_function(say_moo, "say_moo")
r.m_server.serve_forever()

