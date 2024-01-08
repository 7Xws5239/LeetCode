'''
给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。

请注意 ，必须在不复制数组的情况下原地对数组进行操作。
'''
from typing import List

#############################标准解法#############################
###思路： 使用两个指针，一个用于遍历数组，另一个用于记录最后一个非零元素的位置。这种方法可以确保所有非零元素的相对顺序保持不变，同时将所有零移动到数组的末尾。
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        # 记录最后一个非零元素的位置
        lastNonZeroFoundAt = 0

        # 遍历数组
        for i in range(len(nums)):
            # 如果当前元素不是零，将它移动到 lastNonZeroFoundAt 的位置
            if nums[i] != 0:
                nums[lastNonZeroFoundAt] = nums[i]
                lastNonZeroFoundAt += 1

        # 将剩余的位置都填充为零
        for i in range(lastNonZeroFoundAt, len(nums)):
            nums[i] = 0
#############################标准解法#############################


# class Solution:
#     def moveZeroes(self, nums: List[int]) -> None:
#         """
#         Do not return anything, modify nums in-place instead.
#         """
#         # for i in range(0,len(nums)):
#         #     print(nums[i])
#         # print("xxxxxxxxxxxxxxxxxxx")
        
        
        
#         for i in range(0,len(nums)):
#             if nums[i] == 0:
#                 for j in range(i+1,len(nums)):
#                     nums[j-1] = nums[j]
#                 nums[len(nums)-1] = 0
#         for i in range(0,len(nums)):
#             print(nums[i])
            

#         #############################错误解法#############################
#         # for i in range(0,len(nums)):
#         #     if nums[i] == 0:
#         #         for j in range(i+1,len(nums)):
#         #             nums[j-1] = nums[j]
#         #         nums[len(nums)-1] = 0
#         # for i in range(0,len(nums)):
#         #     print(nums[i])
#         ###这里使用的 i 会让第二次从第二个开始找，这时候会漏掉第一个的为0的判断
#         #############################错误解法#############################

# nums = [0,1,0,3,12]
# nums = [0]  
nums = [0,0,1]                      

sln = Solution()
result = sln.moveZeroes(nums)

