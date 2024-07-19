import java.util.*;

// Class to represent the graph
class Graph {
    private final Map<String, List<Edge>> adjacencyList;

    public Graph() {
        this.adjacencyList = new HashMap<>();
    }

    // Method to add an edge to the graph
    public void addEdge(String source, String target, int weight) {
        this.adjacencyList.putIfAbsent(source, new ArrayList<>());
        this.adjacencyList.get(source).add(new Edge(target, weight));
    }

    // Method to get the adjacency list of a vertex
    public List<Edge> getAdjacencyList(String vertex) {
        return this.adjacencyList.getOrDefault(vertex, new ArrayList<>());
    }

    // Method to get all vertices in the graph
    public Set<String> getVertices() {
        return this.adjacencyList.keySet();
    }
}

// Class to represent an edge in the graph
class Edge {
    String target;
    int weight;

    public Edge(String target, int weight) {
        this.target = target;
        this.weight = weight;
    }

    public String getTarget() {
        return target;
    }

    public int getWeight() {
        return weight;
    }
}

// Class to implement Dijkstra's algorithm
class Dijkstra {
    public static Map<String, Integer> findShortestPath(Graph graph, String start) {
        Map<String, Integer> distances = new HashMap<>();
        PriorityQueue<Edge> priorityQueue = new PriorityQueue<>(Comparator.comparingInt(Edge::getWeight));

        // Initialize distances
        for (String vertex : graph.getVertices()) {
            distances.put(vertex, Integer.MAX_VALUE);
        }
        distances.put(start, 0);
        priorityQueue.add(new Edge(start, 0));

        // Process the graph
        while (!priorityQueue.isEmpty()) {
            Edge current = priorityQueue.poll();
            String currentNode = current.getTarget();
            int currentDistance = current.getWeight();

            if (currentDistance > distances.get(currentNode)) {
                continue;
            }

            for (Edge neighbor : graph.getAdjacencyList(currentNode)) {
                int newDist = currentDistance + neighbor.getWeight();
                if (newDist < distances.get(neighbor.getTarget())) {
                    distances.put(neighbor.getTarget(), newDist);
                    priorityQueue.add(new Edge(neighbor.getTarget(), newDist));
                }
            }
        }

        return distances;
    }
}

public class Main {
    public static void main(String[] args) {
        // Create a graph and add edges
        Graph graph = new Graph();
        graph.addEdge("A", "B", 4);
        graph.addEdge("A", "C", 2);
        graph.addEdge("B", "C", 5);
        graph.addEdge("B", "D", 10);
        graph.addEdge("C", "E", 3);
        graph.addEdge("E", "D", 4);

        // Find the shortest path from vertex A
        Map<String, Integer> distances = Dijkstra.findShortestPath(graph, "A");

        // Print the shortest distances from A
        System.out.println("Shortest distances from A:");
        for (Map.Entry<String, Integer> entry : distances.entrySet()) {
            System.out.println(entry.getKey() + ": " + entry.getValue());
        }
    }
}
