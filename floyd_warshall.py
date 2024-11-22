from typing import List
import numpy as np

def compute_shortest_paths(weight_matrix: List[List[int]]):
    weight_array = np.array(weight_matrix)
    vertex_count = len(weight_array)
    distance_array = np.array([[[float(0) for _ in range(vertex_count)] for _ in range(vertex_count)] for _ in range(vertex_count)])
    distance_array[0] = weight_array
    for intermediate in range(0, vertex_count - 1):
        next_step = intermediate + 1
        for src in range(0, vertex_count):
            for dest in range(0, vertex_count):
                distance_array[next_step][src][dest] = min(
                    distance_array[next_step - 1][src][dest],
                    distance_array[next_step - 1][src][intermediate] + distance_array[next_step - 1][intermediate][dest]
                )

        print(f"\nDistance Matrix After Step {next_step}")
        print(distance_array[next_step])
    return distance_array[vertex_count - 1]

# Recursive implementation of Floyd-Warshall algorithm
def recursive_shortest_paths(weight_matrix: List[List[int]], step: int):
    vertex_count = len(weight_matrix)
    current_distance = [[float(0) for _ in range(vertex_count)] for _ in range(vertex_count)]
    current_distance = np.array(current_distance)
    for src in range(vertex_count):
        for dest in range(vertex_count):
            current_distance[src][dest] = min(
                weight_matrix[src][dest],
                weight_matrix[src][step] + weight_matrix[step][dest]
            )
    if step == vertex_count - 1:
        return current_distance
    print(f"\nDistance Matrix After Step {step + 1}")
    print(current_distance)
    return recursive_shortest_paths(current_distance, step + 1)

def generate_predecessor_matrix(weight_matrix: List[List[int]]):
    vertex_count = len(weight_matrix)
    predecessor_matrix = [[float(0) for _ in range(vertex_count)] for _ in range(vertex_count)]
    predecessor_matrix = np.array(predecessor_matrix)
    for src in range(vertex_count):
        for dest in range(vertex_count):
            if src != dest and weight_matrix[src][dest] != float('inf'):
                predecessor_matrix[src][dest] = src
            else:
                predecessor_matrix[src][dest] = None
    return predecessor_matrix

if __name__ == "__main__":
    # Example adapted from figure 25.4 in Chapter 25 of Introduction to Algorithms by Cormen et al.
    weights = [[0, 3, 8, float('inf'), -4],
               [float('inf'), 0, float('inf'), 1, 7],
               [float('inf'), 4, 0, float('inf'), float('inf')],
               [2, float('inf'), -5, 0, float('inf')],
               [float('inf'), float('inf'), float('inf'), 6, 0]]

    weight_array = np.array(weights)
    print("\nIterative Shortest Path Calculation")
    print("\nFinal Distance Matrix\n", compute_shortest_paths(weights))
    print("\nRecursive Shortest Path Calculation")
    print("\nFinal Distance Matrix\n", recursive_shortest_paths(weight_array, 0))

    print("\nPredecessor Matrix")
    print(generate_predecessor_matrix(weights))
