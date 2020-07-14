# Time Complexity - O(N^N)
# Space Complexity - O(N)
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n=len(triangle)
        dp = [[0] * (i + 1) for i in range(n)]
        i = n-1
        for j in range(i+1):
            dp[i][j]=triangle[i][j]
        for i in range(n - 2, -1, -1):
            for j in range(i + 1):
                dp[i][j] = min(dp[i+1][j], dp[i+1][j+1]) + triangle[i][j]            
        return dp[0][0]
