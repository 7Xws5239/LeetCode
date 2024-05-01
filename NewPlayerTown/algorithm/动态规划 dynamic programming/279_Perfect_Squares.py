'''
给你一个整数 n ，返回 和为 n 的完全平方数的最少数量 。

完全平方数 是一个整数，其值等于另一个整数的平方；换句话说，其值等于一个整数自乘的积。例如，1、4、9 和 16 都是完全平方数，而 3 和 11 不是。
'''

from typing import List
import math
# 解决这个问题的思路是建立一个动态规划表，其中 dp[i] 表示组成整数 i 所需的最少完全平方数的个数。对于每个整数 i，我们尝试减去一个平方数，并查看剩余部分组成所需的最小平方数个数。
class Solution:
    def numSquares(self, n: int) -> int:
        # 创建动态规划数组，大小为n+1，初始值设置为无穷大，除了dp[0]为0（因为和为0的完全平方数数量为0）
        dp = [float('inf')] * (n + 1)
        dp[0] = 0
        
        # 预计算所有小于等于n的完全平方数
        max_square_index = int(math.sqrt(n)) + 1
        square_nums = [i * i for i in range(1, max_square_index)]
        
        # 填充dp数组
        for i in range(1, n + 1):
            for square in square_nums:
                if i < square:
                    break
                dp[i] = min(dp[i], dp[i - square] + 1)
        
        # 返回和为n的完全平方数的最少数量
        return dp[n]

# 用例测试
sol = Solution()
print(sol.numSquares(12))  # 输出应该是3（4 + 4 + 4）
print(sol.numSquares(13))  # 输出应该是2（4 + 9）
