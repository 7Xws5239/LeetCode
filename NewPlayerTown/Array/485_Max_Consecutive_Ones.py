'''
给定一个二进制数组 nums ， 计算其中最大连续 1 的个数。
'''
from typing import List

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        print()
        count = 0
        after_check_count = 0
        for i in range(0,len(nums)):
            # print(i,nums[i])
            if nums[i] == 1:
                count = count + 1
                after_check_count = count
            elif nums[i] == 0:
                if count > after_check_count:
                    after_check_count = count
                # else:
                #     after_check_count = after_check_count
                count = 0
        
        return after_check_count

# nums = [1,1,0,1,1,1]
nums = [1,0,1,1,0,1]
sln_ins = Solution()
result = sln_ins.findMaxConsecutiveOnes(nums)
print(result)