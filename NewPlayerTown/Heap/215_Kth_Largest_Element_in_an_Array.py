'''
给定整数数组 nums 和整数 k，请返回数组中第 k 个最大的元素。

请注意，你需要找的是数组排序后的第 k 个最大的元素，而不是第 k 个不同的元素。

你必须设计并实现时间复杂度为 O(n) 的算法解决此问题。

 

示例 1:

输入: [3,2,1,5,6,4], k = 2
输出: 5
示例 2:

输入: [3,2,3,1,2,4,5,5,6], k = 4
输出: 4
 

提示：

1 <= k <= nums.length <= 105
-104 <= nums[i] <= 104
'''

from typing import List

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        """
        使用快速选择算法找到数组中第k个最大的元素。
        
        参数:
        nums: List[int] -- 输入的整数数组
        k: int -- 指定的第k大的元素位置
        
        返回:
        int -- 数组中第k个最大的元素
        """
        
        # 将问题转化为找第 len(nums) - k 小的元素
        k = len(nums) - k
        
        def partition(left, right, pivot_index):
            """
            根据枢纽元素对数组进行分区。
            
            参数:
            left: int -- 分区的左边界
            right: int -- 分区的右边界
            pivot_index: int -- 枢纽元素的索引
            
            返回:
            int -- 分区后枢纽元素的最终位置
            """
            pivot = nums[pivot_index]
            # 先把枢纽元素交换到末尾
            nums[pivot_index], nums[right] = nums[right], nums[pivot_index]
            
            store_index = left
            for i in range(left, right):
                if nums[i] < pivot:
                    nums[store_index], nums[i] = nums[i], nums[store_index]
                    store_index += 1
            
            # 把枢纽元素移动到其最终位置
            nums[right], nums[store_index] = nums[store_index], nums[right]
            return store_index
        
        def select(left, right):
            """
            找到并返回第k小的元素。
            
            参数:
            left: int -- 查找区间的左边界
            right: int -- 查找区间的右边界
            
            返回:
            int -- 第k小的元素
            """
            if left == right:
                return nums[left]
            
            pivot_index = left
            pivot_index = partition(left, right, pivot_index)
            
            if k == pivot_index:
                return nums[k]
            elif k < pivot_index:
                return select(left, pivot_index - 1)
            else:
                return select(pivot_index + 1, right)
        
        return select(0, len(nums) - 1)

# 示例使用
solution = Solution()
print(solution.findKthLargest([3,2,1,5,6,4], 2))  # 应输出5
print(solution.findKthLargest([3,2,3,1,2,4,5,5,6], 4))  # 应输出4
