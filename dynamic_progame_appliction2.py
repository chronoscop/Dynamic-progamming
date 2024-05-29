'''
The min_distance function computes the minimum edit distance between two strings, also known as the Levenshtein distance. 
The edit distance is the minimum number of operations required to transform one string into another.
'''
def min_distance(word1, word2):

    m, n = len(word1), len(word2)
    
    # dp is a (m+1) x (n+1) 2D list,
    # where dp[i][j] stores the minimum edit distance from the first i characters of word1 to the first j characters of word2.
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    # These two loops initialize the borders of the dynamic programming table.
    # dp[i][0] represents the minimum number of delete operations needed to convert the first i characters of word1 into an empty string, which is i deletions.
    # Similarly, dp[0][j] represents the minimum number of insert operations needed to convert an empty string into the first j characters of word2, which is j insertions.
    for i in range(m + 1):
        dp[i][0] = i
    for j in range(n + 1):
        dp[0][j] = j

    # For each pair of indices (i, j), we check if the i-th character of word1 is the same as the j-th character of word2.
    # If they are the same, then dp[i][j] directly inherits the value of dp[i-1][j-1], as no extra edit is needed for the current character.
    # If they are different, we need to consider three cases:
    #   1. dp[i-1][j] + 1: the minimum edit distance from the first i-1 characters of word1 to the first j characters of word2, plus one delete operation on the i-th character of word1.
    #   2. dp[i][j-1] + 1: the minimum edit distance from the first i characters of word1 to the first j-1 characters of word2, plus one insert operation on the j-th character of word2.
    #   3. dp[i-1][j-1] + 1: the minimum edit distance from the first i-1 characters of word1 to the first j-1 characters of word2, plus one replace operation from the i-th character of word1 to the j-th character of word2.
    
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if word1[i - 1] == word2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = 1 + min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1])

    return dp[m][n]

str1 = "alice"
str2 = "al"
print(min_distance(str1, str2))  # output 3
