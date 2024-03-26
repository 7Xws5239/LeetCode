'''
给定两个字符串 s 和 t ，它们只包含小写字母。

字符串 t 由字符串 s 随机重排，然后在随机位置添加一个字母。

请找出在 t 中被添加的字母。

 

示例 1：

输入：s = "abcd", t = "abcde"
输出："e"
解释：'e' 是那个被添加的字母。
示例 2：

输入：s = "", t = "y"
输出："y"
 

提示：

0 <= s.length <= 1000
t.length == s.length + 1
s 和 t 只包含小写字母
'''

# 首先，我们需要导入类型提示功能，以便我们可以指定输入的字符串类型。
from typing import str

# 定义Solution类
class Solution:
    # 定义findTheDifference方法，该方法接受两个字符串s和t作为参数，并返回一个字符串。
    def findTheDifference(self, s: str, t: str) -> str:
        # 初始化一个计数器变量，用于存储字符串s中每个字符的出现次数。
        # 我们将使用Python的字典来存储这个计数，其中键是字符，值是该字符在s中出现的次数。
        counter = {}
        
        # 遍历字符串s中的每个字符。
        for char in s:
            # 如果字符已经在计数器字典中，增加该字符的计数。
            # 否则，将该字符添加到字典中，并将其计数设置为1。
            if char in counter:
                counter[char] += 1
            else:
                counter[char] = 1
        
        # 现在，遍历字符串t中的每个字符。
        for char in t:
            # 如果字符不在计数器字典中，或者字符的计数已经减到0，
            # 这意味着这是被添加的字符，直接返回这个字符。
            if char not in counter or counter[char] == 0:
                return char
            # 否则，减少字符的计数，因为它在字符串s中也有出现。
            else:
                counter[char] -= 1

# 示例代码，如何使用上面定义的类和方法。
if __name__ == "__main__":
    # 创建Solution类的实例。
    solution = Solution()
    
    # 调用findTheDifference方法并打印结果，以找出被添加的字母。
    print(solution.findTheDifference("abcd", "abcde"))  # 应该输出: "e"
    print(solution.findTheDifference("", "y"))  # 应该输出: "y"
