'''
给你一个整数数组 nums ，数组中的元素 互不相同 。返回该数组所有可能的
子集
（幂集）。

解集 不能 包含重复的子集。你可以按 任意顺序 返回解集。
'''

from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        """
        使用深度优先搜索生成所有可能的子集。

        :param nums: List[int] 输入的整数数组，元素互不相同
        :return: List[List[int]] 数组的所有可能子集
        """
        # 结果列表
        result = []
        
        def dfs(index=0, path=[]):
            """
            深度优先搜索函数。

            :param index: int 当前递归到的nums的索引
            :param path: List[int] 当前路径（子集）
            """
            # 将当前路径的副本添加到结果中，这里每次递归调用都会保存当前路径的状态
            result.append(path.copy())
            
            # 遍历从index开始的nums的每个元素
            for i in range(index, len(nums)):
                # 将nums[i]添加到路径中
                path.append(nums[i])
                # 递归深入到下一层
                dfs(i + 1, path)
                # 回溯，移除路径中最后一个元素
                path.pop()
        
        # 从索引0和空路径开始深度优先搜索
        dfs()
        return result

# 示例用法
sol = Solution()
nums = [1, 2, 3]
print(sol.subsets(nums))
# 输出: [
#   [], [1], [1, 2], [1, 2, 3], [1, 3], [2], [2, 3], [3]
# ]
