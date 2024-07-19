# Python program to solve Knapsack problem using dynamic programming

def knapsack(weights, values, capacity):
    n = len(weights)
    dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]

    # Build table dp[][] in bottom up manner
    for i in range(n + 1):
        for w in range(capacity + 1):
            if i == 0 or w == 0:
                dp[i][w] = 0
            elif weights[i - 1] <= w:
                dp[i][w] = max(values[i - 1] + dp[i - 1][w - weights[i - 1]], dp[i - 1][w])
            else:
                dp[i][w] = dp[i - 1][w]

    # Return the maximum value that can be put in a knapsack of capacity
    return dp[n][capacity]

def main():
    values = [60, 100, 120]
    weights = [10, 20, 30]
    capacity = 50
    print("Maximum value in knapsack =", knapsack(weights, values, capacity))

if __name__ == "__main__":
    main()
