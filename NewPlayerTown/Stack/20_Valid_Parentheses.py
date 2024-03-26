'''
给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串 s ，判断字符串是否有效。

有效字符串需满足：

左括号必须用相同类型的右括号闭合。
左括号必须以正确的顺序闭合。
每个右括号都有一个对应的相同类型的左括号。
 

示例 1：

输入：s = "()"
输出：true
示例 2：

输入：s = "()[]{}"
输出：true
示例 3：

输入：s = "(]"
输出：false
 

提示：

1 <= s.length <= 104
s 仅由括号 '()[]{}' 组成
'''

class Solution:
    def isValid(self, s: str) -> bool:
        # 初始化一个栈
        stack = []
        # 建立一个字典，用来快速找到匹配的左括号
        mapping = {")": "(", "}": "{", "]": "["}
        
        # 遍历字符串中的每个字符
        for char in s:
            # 如果字符是右括号
            if char in mapping:
                # 弹出栈顶元素，如果栈为空，则用一个不可能出现的字符
                top_element = stack.pop() if stack else '#'
                # 如果弹出的元素与当前右括号不匹配，则返回False
                if mapping[char] != top_element:
                    return False
            else:
                # 如果是左括号，就放入栈中
                stack.append(char)
        
        # 如果栈为空，则说明所有括号都正确匹配了，返回True；否则返回False
        return not stack

# 创建一个Solution实例
solution = Solution()
# 测试示例
test_cases = ["()", "()[]{}", "(]"]

# 对每个测试示例调用isValid方法，并打印结果
results = {test_case: solution.isValid(test_case) for test_case in test_cases}
print(results)
