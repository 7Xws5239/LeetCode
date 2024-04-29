'''
峰值元素是指其值严格大于左右相邻值的元素。

给你一个整数数组 nums，找到峰值元素并返回其索引。数组可能包含多个峰值，在这种情况下，返回 任何一个峰值 所在位置即可。

你可以假设 nums[-1] = nums[n] = -∞ 。

你必须实现时间复杂度为 O(log n) 的算法来解决此问题。
'''

from typing import List

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        """
        使用二分查找找到数组中的一个峰值元素的索引。
        
        :param nums: List[int] 一个可能包含多个峰值的整数数组
        :return: int 返回任意一个峰值的索引
        """
        left, right = 0, len(nums) - 1
        
        while left < right:
            mid = (left + right) // 2
            # 比较中间元素和它右边的元素
            if nums[mid] < nums[mid + 1]:
                # 如果右边的元素更大，说明峰值在右半部分
                left = mid + 1
            else:
                # 否则峰值在左半部分，包括当前中点
                right = mid
        
        # 循环结束时，left == right，指向峰值元素
        return left

# 示例用法
sol = Solution()
nums = [1, 2, 1, 3, 5, 6, 4]
print(sol.findPeakElement(nums))  # 输出可能是 1 或 5，因为 2 和 6 是峰值元素
