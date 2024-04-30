'''
给你一个整数数组 nums ，数组中的元素 互不相同 。返回该数组所有可能的
子集
（幂集）。

解集 不能 包含重复的子集。你可以按 任意顺序 返回解集。
'''

from typing import List
# 这种方法确保了每个子集都被精确地探索一次，而且每种组合都只生成一次，有效避免了重复。
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        """
        生成一个整数数组的所有可能子集。

        :param nums: List[int] 一个整数数组，元素互不相同
        :return: List[List[int]] 数组的所有可能子集
        """
        result = []
        
        def backtrack(start=0, current_subset=[]):
            """
            回溯函数，用于生成子集。

            :param start: int 当前选择的起始位置
            :param current_subset: List[int] 当前正在构建的子集
            """
            # 将当前构建的子集添加到结果列表中
            # 在每次调用时首先添加，确保包括空集和所有中间组合
            result.append(current_subset[:])
            
            # 从start开始遍历数组，尝试包含当前元素到子集中
            for i in range(start, len(nums)):
                current_subset.append(nums[i])
                # 递归调用，注意更新start为i + 1，避免重复使用同一元素
                backtrack(i + 1, current_subset)
                # 回溯，移除当前元素，尝试下一个元素
                current_subset.pop()
        
        # 从索引0开始生成子集
        backtrack()
        return result

# 示例用法
sol = Solution()
nums = [1, 2, 3]
print(sol.subsets(nums))
# 输出: [
#   [], [1], [1, 2], [1, 2, 3], [1, 3], [2], [2, 3], [3]
# ]
