def rod_cutting(prices, n):
    # Initialize a list 'dp' with '0' as elements to store the maximum revenue for each rod length
    dp = [0] * (n + 1)
    
    # Iterate through each rod length from 1 to 'n'
    for i in range(1, n + 1):
        # Initialize 'max_val' with negative infinity
        max_val = float('-inf')
        
        # Iterate through each possible cut position 'j' for the current rod length 'i'
        for j in range(i):
            # Calculate the maximum revenue by considering the price of the rod and the maximum revenue for the remaining rod
            max_val = max(max_val, prices[j] + dp[i - j - 1])
        
        # Store the maximum revenue for the current rod length 'i' in the 'dp' list
        dp[i] = max_val
        
    # Return the maximum revenue for the rod of length 'n'
    return dp[n]

# Example usage
prices = [1, 5, 8, 9, 10, 17, 17, 20]
n = 8
print(f"Maximum obtainable value is {rod_cutting(prices, n)}")
