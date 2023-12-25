from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i, num1 in enumerate(nums):
            for j, num2 in enumerate(nums):
                if i != j and num1 + num2 == target:
                    return [i, j]
        # print("")

sln_instance = Solution()

result = sln_instance.twoSum(nums=[2, 7, 11, 15, 1, 8], target=9)

print("result: ", result)