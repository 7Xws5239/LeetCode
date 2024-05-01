'''
在一个由 '0' 和 '1' 组成的二维矩阵内，找到只包含 '1' 的最大正方形，并返回其面积。
'''
# 这个问题可以通过动态规划方法来解决，核心思想是利用一个二维 dp 数组来记录每个点作为正方形右下角时最大正方形的边长。我们逐个遍历矩阵中的元素，并更新 dp 数组。如果当前元素是 '1'，它能形成的最大正方形的边长将基于它的左侧、上方和左上角（对角线方向）的值。

from typing import List

class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        # 获取矩阵的行数和列数
        if not matrix:
            return 0
        rows, cols = len(matrix), len(matrix[0])
        
        # 创建dp数组，并加上一行一列的边界，以简化边界条件的处理
        dp = [[0] * (cols + 1) for _ in range(rows + 1)]
        max_side = 0  # 记录最大边长
        
        # 遍历原矩阵
        for i in range(1, rows + 1):
            for j in range(1, cols + 1):
                # 只有当当前元素是'1'时，才考虑正方形
                if matrix[i-1][j-1] == '1':
                    # 状态转移方程
                    dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
                    # 更新最大边长
                    if dp[i][j] > max_side:
                        max_side = dp[i][j]
        
        # 最大正方形的面积是最大边长的平方
        return max_side * max_side

# 用例测试
sol = Solution()
matrix = [
    ["1", "0", "1", "0", "0"],
    ["1", "0", "1", "1", "1"],
    ["1", "1", "1", "1", "1"],
    ["1", "0", "0", "1", "0"]
]
print(sol.maximalSquare(matrix))  # 输出应该是4，因为最大正方形边长为2
