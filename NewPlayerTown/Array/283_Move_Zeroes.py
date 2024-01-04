'''
给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。

请注意 ，必须在不复制数组的情况下原地对数组进行操作。
'''
from typing import List
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # for i in range(0,len(nums)):
        #     print(nums[i])
        # print("xxxxxxxxxxxxxxxxxxx")
        
        
        for i in range(0,len(nums)):
            if nums[i] == 0:
                for j in range(i+1,len(nums)):
                    nums[j-1] = nums[j]
                nums[len(nums)-1] = 0
        for i in range(0,len(nums)):
            print(nums[i])
            

        #############################错误解法#############################
        # for i in range(0,len(nums)):
        #     if nums[i] == 0:
        #         for j in range(i+1,len(nums)):
        #             nums[j-1] = nums[j]
        #         nums[len(nums)-1] = 0
        # for i in range(0,len(nums)):
        #     print(nums[i])
        ###这里使用的 i 会让第二次从第二个开始找，这时候会漏掉第一个的为0的判断
        #############################错误解法#############################

# nums = [0,1,0,3,12]
# nums = [0]  
nums = [0,0,1]                      

sln = Solution()
result = sln.moveZeroes(nums)

