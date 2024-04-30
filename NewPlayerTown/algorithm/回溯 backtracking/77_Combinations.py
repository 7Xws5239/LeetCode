'''
给定两个整数 n 和 k，返回范围 [1, n] 中所有可能的 k 个数的组合。

你可以按 任何顺序 返回答案。
'''

from typing import List
# 使用回溯法解决组合问题能够确保所有可能的组合都被探索到，并且通过适当的剪枝保证了效率。
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        """
        生成从1到n的数字中所有可能的k个数字的组合。

        :param n: int 数字范围的上界
        :param k: int 组合中的数字数量
        :return: List[List[int]] 所有可能的组合
        """
        result = []
        
        def backtrack(start=1, current_combination=[]):
            """
            回溯函数，用于生成组合。

            :param start: int 当前生成组合的起始数字
            :param current_combination: List[int] 当前正在构建的组合
            """
            # 当前组合的长度等于k时，将其添加到结果列表中
            if len(current_combination) == k:
                result.append(current_combination[:])
                return
            
            # 遍历从start到n的所有数字，尝试加入当前组合
            for i in range(start, n + 1):
                current_combination.append(i)
                # 递归调用，从下一个数字开始生成剩余的组合
                backtrack(i + 1, current_combination)
                # 回溯，移除上一步加入的数字
                current_combination.pop()
        
        # 从数字1开始生成组合
        backtrack()
        return result

# 示例用法
sol = Solution()
n = 4
k = 2
print(sol.combine(n, k))
# 输出: [
#   [1, 2], [1, 3], [1, 4],
#   [2, 3], [2, 4],
#   [3, 4]
# ]
