'''
编写一个函数，其作用是将输入的字符串反转过来。输入字符串以字符数组 s 的形式给出。

不要给另外的数组分配额外的空间，你必须原地修改输入数组、使用 O(1) 的额外空间解决这一问题。
'''
from typing import List
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        这个方法直接在传入的列表s上操作，不返回任何值，实现了字符串的原地反转。
        我们使用双指针技术，一个指针从头开始，另一个从尾开始，逐步向中间移动并交换两指针处的字符。
        
        :param s: 字符列表
        """
        # 初始化两个指针，left指向数组的开始，right指向数组的末尾
        left, right = 0, len(s) - 1 # 这种做法也叫“并行赋值”或者“元组解包”，用于同时初始化两个变量，等价于 left=0 加上 right=len(s)-1
        
        # 当left小于right时，继续执行循环
        while left < right:
            # 交换left和right指向的元素
            s[left], s[right] = s[right], s[left]
            # 将left向右移动
            left += 1
            # 将right向左移动
            right -= 1

# 示例用法
sol = Solution()
input_string = ['h', 'e', 'l', 'l', 'o']
sol.reverseString(input_string)
print(input_string)  # 输出: ['o', 'l', 'l', 'e', 'h']
