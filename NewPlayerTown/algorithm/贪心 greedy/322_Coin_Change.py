'''
给你一个整数数组 coins ，表示不同面额的硬币；以及一个整数 amount ，表示总金额。

计算并返回可以凑成总金额所需的 最少的硬币个数 。如果没有任何一种硬币组合能组成总金额，返回 -1 。

你可以认为每种硬币的数量是无限的。
'''

from typing import List
# 对于这种类型的问题，通常使用动态规划（Dynamic Programming, DP）来解决是最合适的。动态规划可以有效地处理组合总和问题，尤其是在需要找到最小数量的组合时。
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # 初始化一个长度为 amount+1 的数组 dp，每个值设为一个很大的数表示无法达到的状态
        # dp[i] 表示凑成金额 i 所需的最少硬币数量
        dp = [float('inf')] * (amount + 1)
        
        # 凑成金额 0 的最少硬币数量是 0
        dp[0] = 0
        
        # 遍历所有金额，从 1 到 amount
        for i in range(1, amount + 1):
            # 遍历所有硬币
            for coin in coins:
                # 如果当前硬币面额小于或等于当前金额，我们可以尝试使用这枚硬币
                if i >= coin:
                    # 更新 dp[i] 为使用当前硬币和不使用当前硬币的最小值
                    dp[i] = min(dp[i], dp[i - coin] + 1)
        
        # 检查最终的 dp[amount] 是否为无穷大，如果是则返回 -1，表示无法凑成
        return dp[amount] if dp[amount] != float('inf') else -1



# 这个下面用的贪心算法并不是一个正确的方法，提交leetcode也是不能通过的，我认为是饲养员搞错了

'''
虽然贪心算法在某些情况下可能无法提供解决此类问题的最优解，但它能在特定条件下提供较快的解答。
下面是使用贪心算法尝试解决给定的“硬币找零”问题的代码示例，其中包括详细注释。
请注意，这种方法可能无法解决所有情况，因为贪心算法无法保证达到最小硬币数的全局最优解，特别是硬币的组合方式会影响最终结果。
'''
'''
from typing import List

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        """
        使用贪心算法尝试解决硬币找零问题，但请注意这可能不总是返回正确的最小硬币数。
        
        :param coins: List[int] 不同面额的硬币
        :param amount: int 总金额
        :return: int 最少的硬币个数，如果无法凑出则返回-1
        """
        # 对硬币面额进行降序排序
        coins.sort(reverse=True)
        total_coins = 0
        remaining_amount = amount
        
        for coin in coins:
            # 计算当前硬币最多能使用多少个
            if remaining_amount <= 0:
                break
            count = remaining_amount // coin
            remaining_amount -= count * coin
            total_coins += count
        
        # 如果余额为0，说明已经凑齐了总金额
        if remaining_amount == 0:
            return total_coins
        else:
            # 如果余额不为0，说明无法凑齐总金额
            return -1

# 示例用法
sol = Solution()
coins = [1, 2, 5]
amount = 11
print(sol.coinChange(coins, amount))  # 输出可能不是最优解

coins = [2]
amount = 3
print(sol.coinChange(coins, amount))  # 输出-1，因为无法凑出总金额
'''