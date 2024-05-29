''' 
Task:
Use dynamic programming to implement a function maxSubArray(nums) that takes an array of integers nums 
as input and returns the sum of the contiguous subarray with the largest sum.
 '''
def maxSubArray(nums):
    # Initialize dp array, dp[i] represents the maximum sum of the subarray ending at nums[i]
    dp = [0] * len(nums)
    dp[0] = nums[0]  # Initialize the first element
    
    # Compute the values of the dp array iteratively
    for i in range(1, len(nums)):
        dp[i] = max(nums[i], dp[i-1] + nums[i])
    # Return the maximum value in the dp array
    return max(dp)

# Test
nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print(maxSubArray(nums))  # Output: 6, corresponding subarray is [4, -1, 2, 1]
