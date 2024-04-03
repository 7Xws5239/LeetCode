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
import heapq
from typing import List

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        """
        寻找数组中第k个最大的元素
        :param nums: List[int] 输入的整数数组
        :param k: int 第k大的元素
        :return: int 第k个最大的元素
        """
        # 初始化一个空堆
        heap = []
        # 遍历数组中的前k个元素，构建大小为k的最小堆
        for i in range(k):
            heapq.heappush(heap, nums[i])
        
        # 继续遍历数组中剩余的元素
        for i in range(k, len(nums)):
            # 如果当前元素大于堆顶元素，替换之
            if nums[i] > heap[0]:
                heapq.heappop(heap)  # 弹出堆顶最小元素
                heapq.heappush(heap, nums[i])  # 加入当前元素
                
        # 最终，堆顶元素即为第k个最大元素
        return heap[0]

# # # 测试代码
# # if __name__ == '__main__':
# #     solution = Solution()
# #     print(solution.findKthLargest([3,2,1,5,6,4], 2))  # 输出: 5
# #     print(solution.findKthLargest([3,2,3,1,2,4,5,5,6], 4))  # 输出: 4


######################################## 饲养员的解法

# from heapq import heapify, heappush, heappop

# class Solution:
#     # Leetcode 215. Kth Largest Element in an Array
#     # Heap
#     # N is the size of nums
#     # Time Complexity: O(NlogK)
#     # Space Complexity: O(N)
#     def findKthLargest(self, nums: List[int], k: int) -> int:
#         minheap = []
#         heapify(minheap)
#         for num in nums:
#             heappush(minheap, num)
#             if len(minheap) > k:
#                 heappop(minheap)
#         return minheap[0]
