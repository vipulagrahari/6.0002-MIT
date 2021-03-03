#Class Node and Edge 
class node(object):
    def __init__(self, name):
        name = self.name
    def get_name(self):
        return self.name 
    def __str__(self):
        return self.name

class Edge(object):     
    def __init__(self, src, dest):
        src = self.src
        des = self.dest
    def get_source(self):
        return self.src 
    def get_destination(self):
        return self.dest
    def __str__(self):
        return self.src.get_name() + "-->" + self.dest.get_name()

class weighted_edge(Edge):
    def __init__(self, src, dest, weight = 1.0):
        src = self.src
        dest = self.dest
        weight = self.weight
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
        if node in nodes:
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
    def Children_of(self):
        return self.edges[node]
    def has_node(self):
        return node in self.edges
    def get_node(self, name):
        for n in self.nodes:
            if n.get_name() == name:

    def __str__(self):
        result = ''
        for src in self.nodes:
            for dest in self.edges[src]:
                result = result + src.getName() + '->' + dest.get_name() + "\n"
        return result[:-1] 

Class Graph(Diagraph):
    def add_edge(self, edge):
        Diagraph.add_edge(edge)
        rev =  Edge(edge.get_destination(), edge.get_source())  
        Diagraph.add_edge(self, rev)
