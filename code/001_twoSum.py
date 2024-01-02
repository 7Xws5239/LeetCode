'''
给定一个整数数组 nums 和一个整数目标值 target，请你在该数组中找出 和为目标值 target  的那 两个 整数，并返回它们的数组下标。

你可以假设每种输入只会对应一个答案。但是，数组中同一个元素在答案里不能重复出现。

你可以按任意顺序返回答案。
'''

############################################################################### My Solution ###############################################################################


###########################################################################################################################################################################

############################################################################### My Solution ###############################################################################
# from typing import List
# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         print()
#         nums_length = nums.__len__()
#         for i in range(0,nums_length-1):
#             for j in range(i+1,nums_length):
#                 if target == nums[i] +nums[j]:
#                     print(i,j)
#                     return i,j
#         # print(nums_length)
#         # for 
#         # for i in nums:
#         #     for j in nums:
#         #         nums[i]=nums

# sln_instance = Solution()

# nums = [11,15,2,7]
# target = 9
# sln_instance.twoSum(nums,target)

# # for i in range(1,6):
# #     print(i)

###########################################################################################################################################################################

############################################################################### 优化后 #####################################################################################
# from typing import List
# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         for i in range(0,len(nums)-1):
#             for j in range(i+1,len(nums)):
#                 if target == nums[i] +nums[j]:
#                     return i,j

# sln_instance = Solution()

# nums = [11,15,2,7]
# target = 9
# result = sln_instance.twoSum(nums,target)
# print(result)

###########################################################################################################################################################################

############################################################################### Better Choice #############################################################################

#上面的方案执行时间 1836ms，而这个方案执行时间 36ms，差距太大了，必须学会

from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = {}

#---------------------------------------错误写法1-------------------
# from typing import List
# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         hash_map = {}
#         for i, nums_value in enumerate(nums): #这种处理方式会导致对于同样的key，后面的索引会覆盖前面的索引
#             hash_map[nums_value] = i
#         print(hash_map)
#         for key, index in hash_map.items(): #这个前面是key，后面是value，后面实际上是索引编号
#             complement = target - key
#             if (complement in hash_map) and (hash_map[complement]!=index): #这边右边的限制是防止自己和自己相加

#                 return index,hash_map[complement]
# #这种写法处理不了同样key的问题，后面的index会覆盖前面的，导致结果出问题。
#---------------------------------------错误写法1-------------------
            

#---------------------------------------错误写法2-------------------
# from typing import List
# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         hash_map = {}
#         for i, nums_value in enumerate(nums):
#             hash_map[i] = nums_value
#         for i, nums_value in nums:
#             complement = target - nums_value
#             if complement in hash_map:
#                 return i,

        
#         print(hash_map)
# #这种写法只是对于List内容的简单重复，但并不适用于这个问题。
# #我们最终需要拿到下标，因此也需要可以简单地获取到下标的方法。
#---------------------------------------错误写法-------------------

sln_instance = Solution()
# nums = [11,15,2,7]
# nums = [2,7,11,5]
# nums = [3,2,4]
nums = [3,3]
target = 6
result = sln_instance.twoSum(nums, target)
print(result)





###########################################################################################################################################################################

