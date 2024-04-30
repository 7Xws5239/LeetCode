'''
给你一个非负整数数组 nums ，你最初位于数组的 第一个下标 。数组中的每个元素代表你在该位置可以跳跃的最大长度。

判断你是否能够到达最后一个下标，如果可以，返回 true ；否则，返回 false 。
'''

from typing import List

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        """
        使用贪心算法判断是否能到达数组的最后一个下标。

        :param nums: List[int] 每个元素表示在该位置可以跳跃的最大长度
        :return: bool 返回是否能到达最后一个下标
        """
        n = len(nums)
        max_reach = 0  # 初始化最远能到达的位置

        for i in range(n):
            if i > max_reach:
                # 如果当前位置已经超过了之前计算的最远能到达的位置，返回False
                return False
            # 更新最远能到达的位置
            max_reach = max(max_reach, i + nums[i])
            if max_reach >= n - 1:
                # 如果最远能到达的位置已经超过或等于最后一个下标，返回True
                return True
        
        return max_reach >= n - 1

# 示例用法
sol = Solution()
nums = [2, 3, 1, 1, 4]
print(sol.canJump(nums))  # 输出: True

nums = [3, 2, 1, 0, 4]
print(sol.canJump(nums))  # 输出: False
