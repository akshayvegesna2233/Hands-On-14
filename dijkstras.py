class Link:
    def __init__(self, source, target, cost):
        self.source = source
        self.target = target
        self.cost = cost

class Vertex:
    def __init__(self, identifier):
        self.identifier = identifier
        self.min_cost = float('inf')
        self.previous = None

def relax_link(source, target, cost):
    if target.min_cost > source.min_cost + cost:
        target.min_cost = source.min_cost + cost
        target.previous = source

def initialize_vertices(graph, start_vertex):
    for vertex in graph.vertices:
        vertex.min_cost = float('inf')
        vertex.previous = None
    start_vertex.min_cost = 0

def extract_lowest_cost(queue):
    lowest = queue[0]
    for vertex in queue:
        if vertex.min_cost < lowest.min_cost:
            lowest = vertex
    queue.remove(lowest)
    return lowest

def compute_shortest_routes(graph, start_vertex):
    initialize_vertices(graph, start_vertex)
    visited = []
    queue = graph.vertices[:]
    while queue:
        current_vertex = extract_lowest_cost(queue)
        visited.append(current_vertex)
        for neighbor in graph.adjacency_list[current_vertex]:
            relax_link(current_vertex, neighbor, graph.link_weights[(current_vertex, neighbor)])
    return visited

def reconstruct_path(vertex):
    route = []
    while vertex:
        route.append(vertex.identifier)
        vertex = vertex.previous
    route.reverse()
    return route

class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.adjacency_list = {}
        self.link_weights = {}
        for vertex in vertices:
            self.adjacency_list[vertex] = []

    def add_link(self, source, target, cost):
        if source not in self.adjacency_list.keys():
            self.adjacency_list[source] = [target]
        else:
            self.adjacency_list[source].append(target)
        self.link_weights[(source, target)] = cost

    def __str__(self):
        print("\n ---Adjacency List---")
        for vertex in self.adjacency_list.keys():
            print(vertex.identifier, end=": ")
            for neighbor in self.adjacency_list[vertex]:
                print(neighbor.identifier, end=" ")
            print("\b")
        return "---End of Adjacency List---\n"


if __name__ == "__main__":
    # Example adapted from figure 24.6 in Introduction to Algorithms by Cormen et al.
    # s: 0, t: 1, x: 2, y: 3, z: 4

    vertices = [Vertex(i) for i in range(5)]

    links = [Link(vertices[0], vertices[1], 10),
             Link(vertices[0], vertices[3], 5),
             Link(vertices[1], vertices[2], 1),
             Link(vertices[1], vertices[3], 2),
             Link(vertices[2], vertices[4], 4),
             Link(vertices[3], vertices[1], 3),
             Link(vertices[3], vertices[2], 9),
             Link(vertices[3], vertices[4], 2),
             Link(vertices[4], vertices[0], 7),
             Link(vertices[4], vertices[2], 6)]

    graph = Graph(vertices)
    for link in links:
        graph.add_link(link.source, link.target, link.cost)
    shortest_routes = compute_shortest_routes(graph, vertices[0])
    print("Vertex | Min Cost | Path")
    print("-------------------------")
    for vertex in shortest_routes:
        path = reconstruct_path(vertex)
        print(f"   {vertex.identifier}   |    {vertex.min_cost}    | {'->'.join(map(str, path))}")
