'''
给定一个不含重复数字的数组 nums ，返回其 所有可能的全排列 。你可以 按任意顺序 返回答案。
'''

from typing import List
# 这种方法的核心在于回溯和撤销操作，确保所有可能的排列都能被正确地探索到。
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        """
        使用回溯法生成数组的所有可能全排列。

        :param nums: List[int] 不含重复数字的数组
        :return: List[List[int]] 所有可能的全排列
        """
        result = []
        
        def backtrack(first=0):
            """
            回溯函数，生成从索引 first 开始的所有排列。

            :param first: int 当前考虑交换的数组索引
            """
            # 如果当前索引为数组的长度，说明已经形成了一个完整的排列
            if first == len(nums):
                result.append(nums[:])
                return
            
            # 递归地在每个位置放置每个数字
            for i in range(first, len(nums)):
                # 将当前元素交换到第一个位置
                nums[first], nums[i] = nums[i], nums[first]
                # 使用 next 元素来填充剩余的位置
                backtrack(first + 1)
                # 回溯，撤销之前的交换
                nums[first], nums[i] = nums[i], nums[first]
        
        backtrack()
        return result

# 示例用法
sol = Solution()
nums = [1, 2, 3]
print(sol.permute(nums))
# 输出: [
#   [1, 2, 3], [1, 3, 2],
#   [2, 1, 3], [2, 3, 1],
#   [3, 1, 2], [3, 2, 1]
# ]
