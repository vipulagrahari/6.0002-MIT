#Class Node and Edge 
class node(object):
    def __init__(self, name):
        self.name = name
    def get_name(self):
        return self.name 
    def __str__(self):
        return self.name

class Edge(object):     
    def __init__(self, src, dest):
        self.src = src 
        self.dest = dest
    def get_source(self):
        return self.src 
    def get_destination(self):
        return self.dest
    def __str__(self):
        return self.src.get_name() + "-->" + self.dest.get_name()

class weighted_edge(Edge):
    def __init__(self, src, dest, weight = 1.0):
        self.src = src 
        self.dest = dest
        self.weight = weight
    def get_weight(self):
        return self.weight
    def __str__(self):
        return self.src.get_name() + "->(" + str(self.weight) + ")" + self.dest.get_name()


#Diagraphs 
class Diagraph(object):
    def __init__(self):
        self.nodes = []
        self.edges = {}
    def add_node(self, node):
        if node in self.nodes:
            raise ValueError("Node already present!!")
        else:
            self.nodes.append(node)
            self.edges[node] = []
    def add_edge(self, edge):
        src = edge.get_source()
        dest = edge.get_destination()
        if not (src in self.nodes and dest in self.nodes):
            raise ValueError("These places do not exist!")
        self.edges[src].append(dest)
    def Children_of(self, node):
        return self.edges[node]
    def has_node(self):
        return node in self.edges
    def get_node(self, name):
        for n in self.nodes:
            if n.get_name() == name:
                return name
    def __str__(self):
        result = ''
        for src in self.nodes:
            for dest in self.edges[src]:
                result = result + src.getName() + '->' + dest.get_name() + "\n"
        return result[:-1] 

class Graph(Diagraph):
    def add_edge(self, edge):
        Diagraph.add_edge(edge)
        rev =  Edge(edge.get_destination(), edge.get_source())  
        Diagraph.add_edge(self, rev)


def printPath(path):
    """Assumes path is a list of nodes"""
    result = '' 
    for i in range(len(path)):
        result = result + str(path[i])
        if i != len(path) - 1: 
            result = result + '->' 
    return result 
def DFS(graph, start, end, path, shortest, toPrint = False):
    """Assumes graph is a Digraph; start and end are nodes;path and shortest are lists of nodesReturns a shortest path from start to end in graph"""
    path = path + [start]
    if toPrint: 
        print('Current DFS path:', printPath(path))
    if start == end:
        return path
    for node in graph.Children_of(start):
        if node not in path: #avoid cycles
            if shortest == None or len(path) < len(shortest):
                newPath = DFS(graph, node, end, path, shortest,toPrint) 
                if newPath != None:
                    shortest = newPath
    return shortest

def shortestPath(graph, start, end, toPrint = False):
    """Assumes graph is a Digraph; start and end are nodesReturns a shortest path from start to end in graph"""
    return DFS(graph, start, end, [], None, toPrint)


printQueue = True

def BFS(graph, start, end, toPrint = False):
    initpath = [start]
    pathqueue = [initpath]
    while len(pathqueue) != 0:
        
        if printQueue:
            print("Queue", len(pathqueue))
            for p in pathqueue:
                print(printPath(p))
        
        tmpPath = pathqueue.pop(0)
        if toPrint:
            print("current bfs Path is", printPath(tmpPath))
            print()
        lastnode = tmpPath[-1]
        if lastnode == end:
            return tmpPath
        for nextnode in graph.Children_of(lastnode):
            newPath = tmpPath + [nextnode]
            pathqueue.append(newPath)
    return None

def testSP():
    nodes = []
    for i in range(6):
        nodes.append(node(str(i)))
    g = Diagraph()
    for n in nodes:
        g.add_node(n)
    g.add_edge(Edge(nodes[0],nodes[1]))
    g.add_edge(Edge(nodes[1],nodes[2]))
    g.add_edge(Edge(nodes[2],nodes[3]))
    g.add_edge(Edge(nodes[2],nodes[4]))
    g.add_edge(Edge(nodes[3],nodes[4]))
    g.add_edge(Edge(nodes[3],nodes[5]))
    g.add_edge(Edge(nodes[0],nodes[2]))
    g.add_edge(Edge(nodes[1],nodes[0]))
    g.add_edge(Edge(nodes[3],nodes[1]))
    g.add_edge(Edge(nodes[4],nodes[0]))  
    
    sp = BFS(g, nodes[0], nodes[5])
    print('Shortest path found by BFS:', printPath(sp))

    ssp = shortestPath(g, nodes[0], nodes[5], toPrint= True)
    print(printPath(ssp))  

testSP()