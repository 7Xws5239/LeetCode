'''
给定一个含有 n 个正整数的数组和一个正整数 target 。

找出该数组中满足其总和大于等于 target 的长度最小的 连续
子数组
 [numsl, numsl+1, ..., numsr-1, numsr] ，并返回其长度。如果不存在符合条件的子数组，返回 0 。
'''

from typing import List

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        """
        使用滑动窗口方法找到数组中总和大于等于 target 的最短连续子数组的长度。
        
        :param target: int 需要达到的目标总和
        :param nums: List[int] 给定的正整数数组
        :return: int 满足条件的最短连续子数组的长度，如果不存在则返回 0
        """
        n = len(nums)
        # 设定一个足够大的初始值，用于更新最小长度
        min_length = float('inf')
        left = 0  # 滑动窗口的左边界
        current_sum = 0  # 当前窗口的总和
        
        for right in range(n):
            # 扩展窗口右边界
            current_sum += nums[right]
            
            # 当当前窗口的总和大于等于目标值时，尝试收缩左边界以找到更小的满足条件的窗口
            while current_sum >= target:
                # 更新最小长度
                min_length = min(min_length, right - left + 1)
                # 收缩窗口的左边界
                current_sum -= nums[left]
                left += 1
        
        # 如果 min_length 未被更新过（仍为初始的无穷大值），说明没有找到满足条件的子数组
        return 0 if min_length == float('inf') else min_length

# 示例用法
sol = Solution()
nums = [2, 3, 1, 2, 4, 3]
target = 7
print(sol.minSubArrayLen(target, nums))  # 输出: 2 (子数组 [4,3] 的长度是 2)
