## reference linking：

1. https://zhuanlan.zhihu.com/p/365698607
2. https://blog.csdn.net/lijunhcn/article/details/132408647

**Note:** **to see a [CN version](CN.md)** |

# Dynamic Programming，DP

Dynamic programming algorithms are based on two main concepts: **overlapping subproblems** and **optimal substructure**. These concepts significantly improve the efficiency of solving complex problems. Below is a detailed introduction to these concepts:

### Overlapping Subproblems

When solving certain problems, the same subproblem may arise multiple times during the computation. Recomputing these subproblems every time they are encountered increases the time and complexity of the solution. Dynamic programming stores the solutions of these subproblems (usually in an array or a hash table) so that each subproblem is solved only once, saving computational resources. For example, in calculating the Fibonacci sequence, direct recursion results in a lot of redundant calculations, whereas dynamic programming saves the computed results to avoid this redundancy.

### Optimal Substructure

A problem has an optimal substructure if the optimal solution to the problem contains the optimal solutions to its subproblems. This means that the overall problem can be solved by combining the solutions to the subproblems. In dynamic programming, we rely on this property to construct the solution. By solving all related subproblems, we ensure that we find the optimal solution to the entire problem. For example, in the knapsack problem, we consider whether to include each item in the knapsack and use the optimal solutions of the subproblems to make the decision.

### Steps to Implement Dynamic Programming

Dynamic programming usually follows these steps:

1. **Define Subproblems**: Break down the original problem into smaller subproblems.
2. **Initialize Base Cases**: Determine the solutions for the simplest subproblems, which are usually the base cases in a recursive algorithm.
3. **Construct the DP Table**: Use a table (usually an array or a 2D array) to store the solutions to the subproblems.
4. **Determine the Order of Filling the Table**: Ensure that when solving a subproblem, all its related subproblems have already been solved.
5. **Transition Equation**: Design an equation (or multiple equations) that describes how to get the solution to a larger problem from the solutions to its subproblems.
6. **Build the Solution**: Construct the final solution from the filled table.

Dynamic programming is not just an algorithm but an algorithm design method that makes solving complex problems more systematic and efficient. By clearly defining subproblems, storing intermediate results, and iteratively building the final solution, dynamic programming can effectively solve various optimization problems.

### Example: Calculating the Fibonacci Sequence

The Fibonacci sequence is a classic recursive problem where each number is the sum of the two preceding ones, defined as follows:

- F(0) = 0
- F(1) = 1
- For n ≥ 2，F(n) = F(n-1) + F(n-2)

### Recursive Method

An intuitive method is to use recursion to directly compute the Fibonacci sequence according to its definition:

```python
def fibonacci_recursive(n):
    if n <= 1:
        return n
    else:
        return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)
```

This method is simple and intuitive but inefficient because it recalculates many subproblems (e.g., F(n-2) is calculated twice when computing F(n) and F(n-1)).
**Note: code also in the file `fibonacci_use_dynamic_programming.py`**

### Dynamic Programming Method

To optimize the above recursive method, we can use dynamic programming. The steps are as follows:

1. **Initialization**: Create an array `dp` where `dp[i]` stores the i-th Fibonacci number.
2. **Base Case Assignment**: Set `dp[0] = 0` and `dp[1] = 1`.
3. **Iterative Calculation**: For all `i` from 2 to `n`, compute `dp[i] = dp[i-1] + dp[i-2]`.

```python
def fibonacci_dp(n):
    if n <= 1:
        return n
    dp = [0] * (n + 1)
    dp[0], dp[1] = 0, 1
    for i in range(2, n + 1):
        dp[i] = dp[i-1] + dp[i-2]
    return dp[n]
```

This method has a time complexity of O(n), and since each subproblem is solved only once and its result is stored, it avoids redundant calculations, significantly improving efficiency.

**Note: See more in the file `fibonacci_use_dynamic_programming.py`**

### Advantages and Limitations of Dynamic Programming

- **Advantages**:
  - **Efficiency**: Avoids redundant calculations, reducing unnecessary computation.
  - **Intuitive**: Solves problems step by step, making it easy to understand and implement.

- **Limitations**:
  - **Space Consumption**: Although space consumption can be reduced using various techniques (such as using a limited number of variables instead of an array), additional storage space may still be required in some cases.

### License:
[MIT License](LICENSE)
