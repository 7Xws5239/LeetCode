'''
给定一个单词列表 words 和一个整数 k ，返回前 k 个出现次数最多的单词。

返回的答案应该按单词出现频率由高到低排序。如果不同的单词有相同出现频率， 按字典顺序 排序。

 

示例 1：

输入: words = ["i", "love", "leetcode", "i", "love", "coding"], k = 2
输出: ["i", "love"]
解析: "i" 和 "love" 为出现次数最多的两个单词，均为2次。
    注意，按字母顺序 "i" 在 "love" 之前。
示例 2：

输入: ["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"], k = 4
输出: ["the", "is", "sunny", "day"]
解析: "the", "is", "sunny" 和 "day" 是出现次数最多的四个单词，
    出现次数依次为 4, 3, 2 和 1 次。
 

注意：

1 <= words.length <= 500
1 <= words[i] <= 10
words[i] 由小写英文字母组成。
k 的取值范围是 [1, 不同 words[i] 的数量]
 

进阶：尝试以 O(n log k) 时间复杂度和 O(n) 空间复杂度解决。
'''

from typing import List
import heapq  # 导入heapq模块，用于实现堆
from collections import Counter  # 导入Counter模块，用于统计单词频率

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        """
        返回前k个出现次数最多的单词
        :param words: List[str] 输入的单词列表
        :param k: int 前k个出现次数最多的单词
        :return: List[str] 出现次数最多的前k个单词
        """
        # 统计每个单词的出现频率
        count = Counter(words)
        
        # 构建一个最小堆，堆中的元素是一个元组，元组的第一个元素是单词出现的频率的负值（这样频率高的单词会在堆的前面）
        # 第二个元素是单词本身，这里使用负值是为了让频率高的元素在堆顶
        # 注意：由于Python的heapq实现是最小堆，为了让频率高的单词排在前面，我们将频率取负值
        # 同时，对于相同频率的单词，我们希望按字典序逆序排列，以确保当它们被pop时，字典序小的在前
        heap = [(-freq, word) for word, freq in count.items()]
        heapq.heapify(heap)  # 将列表转换成堆结构
        
        # 从堆中取出前k个元素，这里直接使用heapq的nlargest方法
        # 由于我们已经通过取负值和逆序排列处理了频率和字典序的问题，所以直接pop即可得到正确顺序
        return [heapq.heappop(heap)[1] for _ in range(k)]

# # 测试代码
# if __name__ == '__main__':
#     solution = Solution()
#     print(solution.topKFrequent(["i", "love", "leetcode", "i", "love", "coding"], 2))  # 预期输出: ["i", "love"]
#     print(solution.topKFrequent(["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"], 4))  # 预期输出: ["the", "is", "sunny", "day"]
