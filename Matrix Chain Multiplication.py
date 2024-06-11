def matrix_chain_order(p):
    # Create a matrix to store the optimal chain length for different sub-chains
    n = len(p) - 1
    m = [[0 for _ in range(n)] for _ in range(n)]
    
    # Iterate through all possible chain lengths
    for L in range(2, n + 1):
        # Iterate through all possible starting points
        for i in range(n - L + 1):
            j = i + L - 1
            # Set the initial value for the cost of this chain to infinity
            m[i][j] = float('inf')
            
            # Iterate through all possible intermediate points
            for k in range(i, j):
                # Calculate the cost of this chain by adding the costs of the left and right sub-chains, plus the product of the sizes of the sub-chains
                q = m[i][k] + m[k + 1][j] + p[i] * p[k + 1] * p[j + 1]
                # If the calculated cost is less than the current cost, update the cost
                if q < m[i][j]:
                    m[i][j] = q
                    
    # Return the optimal cost for the entire chain
    return m[0][n - 1]

# Example usage
p = [1, 2, 3, 4]
print(f"Minimum number of multiplications is {matrix_chain_order(p)}")
