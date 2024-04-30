'''
给你字符串 s 和整数 k 。

请返回字符串 s 中长度为 k 的单个子字符串中可能包含的最大元音字母数。

英文中的 元音字母 为（a, e, i, o, u）。
'''

class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        """
        计算给定字符串中长度为 k 的子字符串可能包含的最大元音字母数。
        
        :param s: str 输入的字符串
        :param k: int 子字符串的长度
        :return: int 最大的元音字母数量
        """
        # 元音字母集合
        vowels = set('aeiou')
        max_count = 0  # 最大元音字母计数
        current_count = 0  # 当前窗口中的元音字母计数

        # 初始化第一个窗口并计算元音数量
        for i in range(k):
            if s[i] in vowels:
                current_count += 1
        max_count = current_count

        # 使用滑动窗口遍历字符串
        for i in range(k, len(s)):
            # 窗口滑动，移出窗口的左端字符，移入窗口的右端字符
            if s[i - k] in vowels:
                current_count -= 1
            if s[i] in vowels:
                current_count += 1
            # 更新最大元音字母数量
            max_count = max(max_count, current_count)

        return max_count

# 示例用法
sol = Solution()
s = "abciiidef"
k = 3
print(sol.maxVowels(s, k))  # 输出: 3
