'''
给定一个大小为 n 的数组 nums ，返回其中的多数元素。多数元素是指在数组中出现次数 大于 ⌊ n/2 ⌋ 的元素。

你可以假设数组是非空的，并且给定的数组总是存在多数元素。
'''

from typing import List
# 这种分治法的时间复杂度是 O(nlogn)，因为每一层递归处理所有元素的时间是 O(n)，而递归树的深度为 logn。这个方法虽然不是最优解（Boyer-Moore投票算法可以在 O(n) 时间复杂度解决这个问题），但它提供了一种理解和处理问题的不同角度。
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        """
        使用分治法找出数组中的多数元素。

        :param nums: List[int] 输入的整数数组
        :return: int 返回数组中的多数元素
        """
        def majorityElementRec(left, right):
            # 基本情况：当区间缩小到只有一个元素时，直接返回该元素
            if left == right:
                return nums[left]

            # 分治法将数组从中间分成两部分
            mid = (left + right) // 2
            left_majority = majorityElementRec(left, mid)
            right_majority = majorityElementRec(mid + 1, right)

            # 如果两边的多数元素相同，则直接返回
            if left_majority == right_majority:
                return left_majority

            # 否则，计算两个候选者在当前区间的出现次数
            left_count = sum(1 for i in range(left, right + 1) if nums[i] == left_majority)
            right_count = sum(1 for i in range(left, right + 1) if nums[i] == right_majority)

            # 返回出现次数较多的那个元素
            return left_majority if left_count > right_count else right_majority

        # 从整个数组的范围开始递归调用
        return majorityElementRec(0, len(nums) - 1)

# 示例用法
sol = Solution()
nums = [2,2,1,1,1,2,2]
print(sol.majorityElement(nums))  # 输出: 2
