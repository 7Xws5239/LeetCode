'''
给定一个单词列表 words 和一个整数 k ，返回前 k 个出现次数最多的单词。

返回的答案应该按单词出现频率由高到低排序。如果不同的单词有相同出现频率， 按字典顺序 排序。
'''
# 前缀树好像是实现不了这个问题，这里记录的是一个比较快速的解决问题的方案，用到了python的一些内置的东西。
from typing import List
import collections

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        # 使用Counter来统计每个单词的出现频率
        count = collections.Counter(words)
        
        # 构建一个列表，包含所有单词，然后按照频率降序和字典序排序
        candidates = list(count.keys())
        candidates.sort(key=lambda w: (-count[w], w))
        
        # 返回前k个最频繁出现的单词
        return candidates[:k]

# 使用方法示例
sol = Solution()
result = sol.topKFrequent(["word", "world", "word", "category", "cat"], 2)
print(result)  # 应该输出 ['word', 'category']
