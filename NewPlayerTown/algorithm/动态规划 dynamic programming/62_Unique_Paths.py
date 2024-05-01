'''
一个机器人位于一个 m x n 网格的左上角 （起始点在下图中标记为 “Start” ）。

机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为 “Finish” ）。

问总共有多少条不同的路径？
'''
# 在动态规划数组中，每个元素代表到达那个点有多少种路径。我们可以从起始点开始，逐步计算到达每个点的路径数。
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # 创建一个二维数组，用于存储到达每个点的路径数量
        # 初始化所有单元格为1，因为从边界到任何边界点只有一条路径
        dp = [[1] * n for _ in range(m)]
        
        # 遍历数组，从第二行第二列开始
        for i in range(1, m):
            for j in range(1, n):
                # 动态规划转移方程：
                # dp[i][j] = dp[i-1][j] + dp[i][j-1]
                # 意味着到达点(i, j)的路径数是从上面来和从左边来的路径数之和
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        
        # 返回到达最右下角的路径数
        return dp[m-1][n-1]

# 用例测试
sol = Solution()
m = 3
n = 7
print(sol.uniquePaths(m, n))  # 输出应该是28
