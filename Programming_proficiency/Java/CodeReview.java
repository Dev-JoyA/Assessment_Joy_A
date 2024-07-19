import java.util.*;
import org.apache.commons.math3.special.Gamma;

public class CodeReview {

    // Calculates the factorial of a complex number using the Gamma function
    public static double complexNumberFactorial(double real, double imag) {
        return Gamma.gamma(real + 1) * Gamma.gamma(imag + 1);
    }

    // Generates a random matrix
    public static int[][] generateRandomMatrix(int rows, int cols, int minVal, int maxVal) {
        Random random = new Random();
        int[][] matrix = new int[rows][cols];
        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < cols; j++) {
                matrix[i][j] = random.nextInt((maxVal - minVal) + 1) + minVal;
            }
        }
        return matrix;
    }

    // Finds the shortest path in a graph using Dijkstra's algorithm
    public static int findOptimalPath(Map<String, Map<String, Integer>> graph, String start, String end) {
        Map<String, Integer> distances = new HashMap<>();
        for (String node : graph.keySet()) {
            distances.put(node, Integer.MAX_VALUE);
        }
        distances.put(start, 0);
        Set<String> visited = new HashSet<>();

        while (visited.size() != graph.size()) {
            String minNode = null;
            for (String node : graph.keySet()) {
                if (!visited.contains(node) && (minNode == null || distances.get(node) < distances.get(minNode))) {
                    minNode = node;
                }
            }

            if (minNode == null) {
                break;
            }

            visited.add(minNode);

            for (Map.Entry<String, Integer> neighborEntry : graph.get(minNode).entrySet()) {
                String neighbor = neighborEntry.getKey();
                int weight = neighborEntry.getValue();
                int newDist = distances.get(minNode) + weight;
                if (newDist < distances.get(neighbor)) {
                    distances.put(neighbor, newDist);
                }
            }
        }

        return distances.get(end);
    }

    public static void main(String[] args) {
        // Demonstrate corrected functions
        double real = 3.0;
        double imag = 4.0;
        double result = complexNumberFactorial(real, imag);
        System.out.println("Factorial of complex number: " + result);

        int[][] matrix = generateRandomMatrix(3, 3, 1, 10);
        System.out.println("Random Matrix:");
        for (int[] row : matrix) {
            System.out.println(Arrays.toString(row));
        }

        Map<String, Map<String, Integer>> graph = new HashMap<>();
        graph.put("A", Map.of("B", 6, "C", 4));
        graph.put("B", Map.of("D", 2, "E", 3));
        graph.put("C", Map.of("F", 5));
        graph.put("D", new HashMap<>());
        graph.put("E", Map.of("F", 1));
        graph.put("F", new HashMap<>());

        int shortestPath = findOptimalPath(graph, "A", "F");
        System.out.println("Shortest path from A to F: " + shortestPath);
    }
}
