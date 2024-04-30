'''
编写一个函数，其作用是将输入的字符串反转过来。输入字符串以字符数组 s 的形式给出。

不要给另外的数组分配额外的空间，你必须原地修改输入数组、使用 O(1) 的额外空间解决这一问题。
'''

# 递归在这里不算是一个好办法，递归可能会导致较大的堆栈使用，而迭代方法更为节省空间，尤其是在处理大数据时。
from typing import List
class Solution:
    def reverseString(self, s: List[str], left=0, right=None) -> None:
        """
        递归地反转字符串数组。这个方法直接在传入的列表s上操作，不返回任何值。
        
        :param s: List[str] 作为字符数组给出的字符串
        :param left: int 开始交换的左边界索引，默认从0开始
        :param right: int 开始交换的右边界索引，默认为列表的最后一个元素的索引
        """
        # 如果right是None，说明是第一次调用，设置right为数组最后一个元素的索引
        if right is None:
            right = len(s) - 1
        
        # 只要左边界索引小于右边界索引，继续递归
        if left < right:
            # 交换当前左右边界索引处的元素
            s[left], s[right] = s[right], s[left]
            # 递归调用，将左边界向右移动一位，右边界向左移动一位
            self.reverseString(s, left + 1, right - 1)

# 示例用法
sol = Solution()
input_string = ['h', 'e', 'l', 'l', 'o']
sol.reverseString(input_string)
print(input_string)  # 输出: ['o', 'l', 'l', 'e', 'h']
