'''
给你一个整数数组 nums ，请你找出一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。

子数组
是数组中的一个连续部分。
'''
# 使用分治法解决这个问题的时间复杂度是 O(nlogn)，因为每次递归都将数组分成两半，并且在合并解时需要线性时间来找到跨越中点的最大子数组和。这种方法虽然不是最优的（Kadane算法可以在 O(n) 时间内解决），但它提供了一种不同的视角和解决问题的方法。
from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        """
        使用分治法计算最大子数组和。

        :param nums: List[int] 输入的整数数组
        :return: int 最大的连续子数组和
        """
        def findMaxCrossingSum(nums, left, mid, right):
            """
            找到跨越中点的最大子数组和。

            :param nums: 数组
            :param left: 左边界索引
            :param mid: 中点索引
            :param right: 右边界索引
            :return: 跨中点的最大子数组和
            """
            # 从中点向左扫描找出最大和
            left_sum = float('-inf')
            current_sum = 0
            for i in range(mid, left - 1, -1):
                current_sum += nums[i]
                if current_sum > left_sum:
                    left_sum = current_sum
            
            # 从中点向右扫描找出最大和
            right_sum = float('-inf')
            current_sum = 0
            for i in range(mid + 1, right + 1):
                current_sum += nums[i]
                if current_sum > right_sum:
                    right_sum = current_sum
            
            # 返回跨中点的最大子数组和
            return left_sum + right_sum

        def maxSubArrayRec(nums, left, right):
            """
            递归计算最大子数组和。

            :param nums: 数组
            :param left: 左边界索引
            :param right: 右边界索引
            :return: 在当前范围内的最大子数组和
            """
            if left == right:
                return nums[left]
            
            mid = (left + right) // 2
            left_max = maxSubArrayRec(nums, left, mid)
            right_max = maxSubArrayRec(nums, mid + 1, right)
            cross_max = findMaxCrossingSum(nums, left, mid, right)

            return max(left_max, right_max, cross_max)
        
        # 初始调用
        return maxSubArrayRec(nums, 0, len(nums) - 1)

# 示例用法
sol = Solution()
nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print(sol.maxSubArray(nums))  # 输出: 6
