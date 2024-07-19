import heapq

# Class to represent the graph
class Graph:
    def __init__(self):
        self.adjacency_list = {}

    # Method to add an edge to the graph
    def add_edge(self, source, target, weight):
        if source not in self.adjacency_list:
            self.adjacency_list[source] = []
        self.adjacency_list[source].append((target, weight))

    # Method to get the neighbors of a vertex
    def get_neighbors(self, vertex):
        return self.adjacency_list.get(vertex, [])

# Function to implement Dijkstra's algorithm
def dijkstra(graph, start):
    distances = {vertex: float('infinity') for vertex in graph.adjacency_list}
    distances[start] = 0
    priority_queue = [(0, start)]

    while priority_queue:
        current_distance, current_vertex = heapq.heappop(priority_queue)

        if current_distance > distances[current_vertex]:
            continue

        for neighbor, weight in graph.get_neighbors(current_vertex):
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances

def main():
    # Create a graph and add edges
    graph = Graph()
    graph.add_edge("A", "B", 4)
    graph.add_edge("A", "C", 2)
    graph.add_edge("B", "C", 5)
    graph.add_edge("B", "D", 10)
    graph.add_edge("C", "E", 3)
    graph.add_edge("E", "D", 4)

    # Find the shortest path from vertex A
    distances = dijkstra(graph, "A")

    # Print the shortest distances from A
    print("Shortest distances from A:")
    for vertex, distance in distances.items():
        print(f"{vertex}: {distance}")

if __name__ == "__main__":
    main()
