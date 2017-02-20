class Graph:

    class Node:
        def __init__(self, n=None, v=False):
            self.visited = v
            self.name = n
            self.nodes=list() # connected nodes

        def connect(self, n=None):
            if isinstance(n, Graph.Node):
                self.nodes.append(n)

        def isVisited(self):
            return  self.visited

        def visit(self):
            self.visited = True

        def printConnections(self):
            for n in self.nodes:
                print("Name: "+n.name+" Visited: "+str(self.visited))


    def __init__(self):
        self.nodes = list()
        for i in range(0, 10):
            n = Graph.Node(str(i)+":node")
            self.nodes.append(n)

        self.nodes[0].connect(self.nodes[1])
        self.nodes[0].connect(self.nodes[2])
        self.nodes[0].connect(self.nodes[3])
        self.nodes[0].connect(self.nodes[4])
        self.nodes[1].connect(self.nodes[5])
        self.nodes[1].connect(self.nodes[6])
        self.nodes[2].connect(self.nodes[7])
        self.nodes[3].connect(self.nodes[8])
        self.nodes[5].connect(self.nodes[1])
        self.nodes[6].connect(self.nodes[1])
        self.nodes[7].connect(self.nodes[1])
        self.nodes[8].connect(self.nodes[0])


    def breadthFirstSearch(self):
        size = len(self.nodes)

        que = []
        while self.nodes:

            p = self.nodes.pop()

            for i in range(0, len(p.nodes)):
                if not p.nodes[i].isVisited():
                    p.nodes[i].visit()
            que.append(p)

        for i in range(0, len(que)):
            self.nodes.append(que[i])


    """Just test function"""
    def print(self):
        for n in self.nodes:
            print("Node: "+n.name+" connections:")
            n.printConnections()


if __name__ == "__main__":
    grp = Graph()
    grp.breadthFirstSearch()
    grp.print()
