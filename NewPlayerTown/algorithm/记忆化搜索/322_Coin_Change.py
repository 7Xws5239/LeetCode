'''
给你一个整数数组 coins ，表示不同面额的硬币；以及一个整数 amount ，表示总金额。

计算并返回可以凑成总金额所需的 最少的硬币个数 。如果没有任何一种硬币组合能组成总金额，返回 -1 。

你可以认为每种硬币的数量是无限的。
'''

from typing import List
# 这是一个典型的动态规划问题，可以通过记忆化搜索（也就是自顶向下的动态规划）来解决。
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # 使用一个字典来存储已经计算过的结果，以避免重复计算
        memo = {}

        def dfs(remaining):
            # 如果剩余金额为0，不需要硬币
            if remaining == 0:
                return 0
            # 如果剩余金额小于0，说明无法凑成该金额
            if remaining < 0:
                return float('inf')
            # 如果已经计算过这个剩余金额，直接返回结果
            if remaining in memo:
                return memo[remaining]
            
            # 初始化最小硬币数量为无穷大
            min_coins = float('inf')
            # 尝试每一种硬币
            for coin in coins:
                # 递归计算剩余金额
                res = dfs(remaining - coin)
                # 更新最小硬币数量
                if res != float('inf'):
                    min_coins = min(min_coins, res + 1)
            
            # 存储计算结果到memo字典
            memo[remaining] = min_coins
            return memo[remaining]

        # 从目标金额开始计算
        result = dfs(amount)
        # 如果结果为无穷大，说明无法凑成该金额，返回-1
        return -1 if result == float('inf') else result

# 用例测试
sol = Solution()
coins = [1, 2, 5]
amount = 11
print(sol.coinChange(coins, amount))  # 输出应该是 3 （5+5+1）
