import xmlrpc.client


with xmlrpc.client.ServerProxy("http://localhost:8000/") as proxy:
    while 1:
        proxy.say_moo()

