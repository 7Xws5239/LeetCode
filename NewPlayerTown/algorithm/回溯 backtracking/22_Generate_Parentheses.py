'''
数字 n 代表生成括号的对数，请你设计一个函数，用于能够生成所有可能的并且 有效的 括号组合。
'''

from typing import List
# 使用回溯法解决这类问题是非常高效的，因为它能够让我们在构建解决方案的过程中剪除无效的解，从而减少了不必要的计算量。
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        """
        生成所有可能的并且有效的括号组合。

        :param n: int 括号对数
        :return: List[str] 所有可能的有效括号组合
        """
        result = []

        def backtrack(s='', left=0, right=0):
            """
            使用回溯法生成有效括号。

            :param s: str 当前括号字符串
            :param left: int 左括号的数量
            :param right: int 右括号的数量
            """
            # 如果字符串长度等于2*n（因为每对括号包括一个左括号和一个右括号），记录当前组合
            if len(s) == 2 * n:
                result.append(s)
                return

            # 如果左括号数量小于n，可以添加一个左括号
            if left < n:
                backtrack(s + '(', left + 1, right)
            
            # 如果右括号数量小于左括号数量，可以添加一个右括号
            if right < left:
                backtrack(s + ')', left, right + 1)

        # 从空字符串开始生成
        backtrack()
        return result

# 示例用法
sol = Solution()
print(sol.generateParenthesis(3))
# 输出: ['((()))', '(()())', '(())()', '()(())', '()()()']
