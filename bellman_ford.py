class Edge:
    def __init__(self, start, end, cost):
        self.start = start
        self.end = end
        self.cost = cost

class Vertex:
    def __init__(self, id):
        self.id = id
        self.min_distance = float('inf')
        self.previous = None

def relax_edge(start, end, cost):
    if end.min_distance > start.min_distance + cost:
        end.min_distance = start.min_distance + cost
        end.previous = start

def prepare_graph(network, start_vertex):
    for vertex in network.vertices:
        vertex.min_distance = float('inf')
        vertex.previous = None
    start_vertex.min_distance = 0

def process_network(network, start_vertex):
    prepare_graph(network, start_vertex)
    for _ in range(len(network.vertices) - 1):
        for (start, end) in network.edge_weights.keys():
            relax_edge(start, end, network.edge_weights[(start, end)])
    for (start, end) in network.edge_weights.keys():
        if end.min_distance > start.min_distance + network.edge_weights[(start, end)]:
            return False
    return True

class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.adjacency_list = {}
        self.edge_weights = {}
        for vertex in vertices:
            self.adjacency_list[vertex] = []

    def add_edge(self, start, end, cost):
        if start not in self.adjacency_list.keys():
            self.adjacency_list[start] = [end]
        else:
            self.adjacency_list[start].append(end)
        self.edge_weights[(start, end)] = cost

    def __str__(self):
        print("\n ---Graph Connections---")
        for vertex in self.adjacency_list.keys():
            print(vertex.id, end=": ")
            for neighbor in self.adjacency_list[vertex]:
                print(neighbor.id, end=" ")
            print("\b")
        return "---End of Connections---\n"


if __name__ == "__main__":
    # Example adapted from figure 24.4 in Introduction to Algorithms by Cormen et al.
    # s: 0, t: 1, x: 2, y: 3, z: 4

    vertices = [Vertex(i) for i in range(5)]

    edges = [Edge(vertices[0], vertices[1], 6),
             Edge(vertices[0], vertices[3], 7),
             Edge(vertices[1], vertices[2], 5),
             Edge(vertices[1], vertices[3], 8),
             Edge(vertices[1], vertices[4], -4),
             Edge(vertices[2], vertices[1], -2),
             Edge(vertices[3], vertices[2], -3),
             Edge(vertices[3], vertices[4], 9),
             Edge(vertices[4], vertices[0], 2),
             Edge(vertices[4], vertices[2], 7)]

    graph = Graph(vertices)
    for edge in edges:
        graph.add_edge(edge.start, edge.end, edge.cost)
    for key in graph.edge_weights.keys():
        print(key, graph.edge_weights[key])
    print(len(graph.edge_weights.keys()))
    print(process_network(graph, vertices[0]))
