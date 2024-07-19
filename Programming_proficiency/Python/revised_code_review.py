import random
import cmath
from collections import defaultdict

def complex_number_factorial(n):
    """
    Calculates the factorial of a complex number using the Gamma function.
    The original implementation was incorrect and inefficient.
    """
    return cmath.gamma(n + 1)

def generate_random_matrix(rows, cols, min_val, max_val):
    """
    Generates a random matrix.
    Ensures that min_val and max_val are integers to avoid type errors.
    """
    matrix = []
    for i in range(rows):
        row = []
        for j in range(cols):
            row.append(random.randint(int(min_val), int(max_val)))
        matrix.append(row)
    return matrix

def find_optimal_path(graph, start, end):
    """
    Finds the shortest path in a graph using Dijkstra's algorithm.
    The original implementation was incorrect for finding the shortest path.
    """
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    visited = set()

    while len(visited) != len(graph):
        min_node = None
        for node in graph:
            if node not in visited and (min_node is None or distances[node] < distances[min_node]):
                min_node = node

        if min_node is None:
            break

        visited.add(min_node)

        for neighbor, weight in graph[min_node].items():
            new_distance = distances[min_node] + weight
            if new_distance < distances[neighbor]:
                distances[neighbor] = new_distance

    return distances[end]

def main():
    # Demonstrate corrected functions
    num = complex(3, 4)
    result = complex_number_factorial(num)
    print(f"Factorial of {num}: {result}")

    matrix = generate_random_matrix(3, 3, 1, 10)
    print("Random Matrix:")
    for row in matrix:
        print(row)

    graph = {
        'A': {'B': 6, 'C': 4},
        'B': {'D': 2, 'E': 3},
        'C': {'F': 5},
        'D': {},
        'E': {'F': 1},
        'F': {}
    }
    shortest_path = find_optimal_path(graph, 'A', 'F')
    print(f"Shortest path from A to F: {shortest_path}")

if __name__ == "__main__":
    main()
