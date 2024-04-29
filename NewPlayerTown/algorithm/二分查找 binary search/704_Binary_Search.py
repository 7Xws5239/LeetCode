'''
给定一个 n 个元素有序的（升序）整型数组 nums 和一个目标值 target  ，写一个函数搜索 nums 中的 target，如果目标值存在返回下标，否则返回 -1。
'''

from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """
        在有序数组中使用二分查找来寻找目标值的索引。
        
        :param nums: List[int] 升序排列的整数数组
        :param target: int 需要查找的目标值
        :return: int 如果找到目标值返回其索引，否则返回 -1
        """
        left, right = 0, len(nums) - 1
        
        while left <= right:
            # 计算中间索引
            mid = (left + right) // 2
            
            # 检查中间值是否为目标值
            if nums[mid] == target:
                return mid
            # 判断目标值是否在左侧半区
            elif nums[mid] > target:
                right = mid - 1
            # 判断目标值是否在右侧半区
            else:
                left = mid + 1
        
        # 如果循环结束还没找到，说明目标值不存在于数组中
        return -1

# 示例用法
sol = Solution()
nums = [-1, 0, 3, 5, 9, 12]
target = 9
print(sol.search(nums, target))  # 输出: 4

target = 2
print(sol.search(nums, target))  # 输出: -1
