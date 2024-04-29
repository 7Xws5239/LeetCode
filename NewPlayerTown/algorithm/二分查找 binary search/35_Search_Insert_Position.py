'''
给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引。如果目标值不存在于数组中，返回它将会被按顺序插入的位置。

请必须使用时间复杂度为 O(log n) 的算法。
'''

from typing import List

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        """
        使用二分查找来确定目标值在有序数组中的位置或应插入的位置。

        :param nums: List[int] 有序数组
        :param target: int 要查找的目标值
        :return: int 目标值在数组中的索引或应插入的位置
        """
        # 定义初始的搜索范围
        left, right = 0, len(nums) - 1
        
        # 当左边界小于等于右边界时进行循环
        while left <= right:
            # 计算中间位置
            mid = (left + right) // 2
            # 如果中间位置的元素等于目标值，直接返回这个位置
            if nums[mid] == target:
                return mid
            # 如果中间位置的元素小于目标值，调整左边界
            elif nums[mid] < target:
                left = mid + 1
            # 如果中间位置的元素大于目标值，调整右边界
            else:
                right = mid - 1
        
        # 如果目标值不在数组中，left 将指向它应当插入的位置
        return left

# 示例用法
sol = Solution()
nums = [1, 3, 5, 6]
target = 5
print(sol.searchInsert(nums, target))  # 输出: 2

target = 2
print(sol.searchInsert(nums, target))  # 输出: 1

target = 7
print(sol.searchInsert(nums, target))  # 输出: 4
