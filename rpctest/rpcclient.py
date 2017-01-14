import xmlrpc.client


with xmlrpc.client.ServerProxy("http://localhost:8000/") as proxy:
    proxy.say_moo()

