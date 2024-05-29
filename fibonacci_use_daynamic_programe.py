# Dynamic Programming Approach
def fibonacci(n):
    # Initialize dp array to store the values of the Fibonacci sequence
    dp = [0] * (n + 1)
    
    # Initialize the first two terms
    dp[0] = 0
    dp[1] = 1
    
    # Iteratively compute the value of the i-th term
    for i in range(2, n + 1):
        dp[i] = dp[i-1] + dp[i-2]
    # Return the value of the n-th term
    return dp[n]

# Test
n = fibonacci(10)
print(n)

# Recursive Approach
def recursion(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return recursion(n-1) + recursion(n-2)
# Test
r = recursion(10)
print(r)
