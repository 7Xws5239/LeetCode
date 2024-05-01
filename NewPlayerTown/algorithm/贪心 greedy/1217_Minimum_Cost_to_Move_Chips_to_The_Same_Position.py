'''
有 n 个筹码。第 i 个筹码的位置是 position[i] 。

我们需要把所有筹码移到同一个位置。在一步中，我们可以将第 i 个筹码的位置从 position[i] 改变为:

position[i] + 2 或 position[i] - 2 ，此时 cost = 0
position[i] + 1 或 position[i] - 1 ，此时 cost = 1
返回将所有筹码移动到同一位置上所需要的 最小代价 。
'''

from typing import List

class Solution:
    def minCostToMoveChips(self, position: List[int]) -> int:
        # 初始化两个计数器，分别用于统计奇数位置和偶数位置的筹码数量
        odd_count = 0
        even_count = 0
        
        # 遍历每个筹码的位置
        for pos in position:
            # 如果位置是奇数，增加奇数计数器
            if pos % 2 == 1:
                odd_count += 1
            # 如果位置是偶数，增加偶数计数器
            else:
                even_count += 1
        
        # 贪心算法的部分：选择将所有筹码移动到奇数位置或偶数位置的成本较小的一方
        # 最小代价是将所有筹码移动到数量较少的位置类别（奇数或偶数）中
        return min(odd_count, even_count)

# 用例测试
sol = Solution()
positions = [1, 2, 3, 4, 5, 6]
print(sol.minCostToMoveChips(positions))  # 输出应该是最小的移动成本
