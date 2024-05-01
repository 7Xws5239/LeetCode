'''
给定一个数组 prices ，它的第 i 个元素 prices[i] 表示一支给定股票第 i 天的价格。

你只能选择 某一天 买入这只股票，并选择在 未来的某一个不同的日子 卖出该股票。设计一个算法来计算你所能获取的最大利润。

返回你可以从这笔交易中获取的最大利润。如果你不能获取任何利润，返回 0 。
'''
# 要解决这个股票买卖问题，我们可以使用动态规划的思想来找到买入和卖出的最佳时机，以获取最大利润。核心思想是在遍历价格数组的同时，记录到目前为止的最低价格，并计算以当前价格卖出所能得到的最大利润。
from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # 初始化最低价格为正无穷大，这样任何一个价格都会小于它
        min_price = float('inf')
        # 初始化最大利润为0
        max_profit = 0
        
        # 遍历价格数组
        for price in prices:
            # 如果当前价格小于目前记录的最低价格，更新最低价格
            if price < min_price:
                min_price = price
            # 如果当前价格与最低价格的差值大于目前的最大利润，更新最大利润
            elif price - min_price > max_profit:
                max_profit = price - min_price
        
        # 返回计算得到的最大利润
        return max_profit

# 用例测试
sol = Solution()
prices = [7, 1, 5, 3, 6, 4]
print(sol.maxProfit(prices))  # 输出应该是5
