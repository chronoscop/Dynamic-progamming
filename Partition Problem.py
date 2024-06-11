def can_partition(nums):
    # Calculate the total sum of the given numbers
    total_sum = sum(nums)
    # If the total sum is not even, it cannot be divided into two equal subsets
    if total_sum % 2 != 0:
        return False
    # Calculate the target sum
    target = total_sum // 2
    # Create a dynamic programming table to store the state of the subproblems
    dp = [False] * (target + 1)
    # Initialize the first state as true
    dp[0] = True
    
    # Iterate through the numbers
    for num in nums:
        # Iterate through the state of the subproblems in reverse order
        for i in range(target, num - 1, -1):
            # Update the state of the subproblem
            dp[i] = dp[i] or dp[i - num]
    
    # Return the state of the target sum
    return dp[target]
# Example usage
nums = [1, 5, 11, 5]
print(f"Can partition: {can_partition(nums)}")
