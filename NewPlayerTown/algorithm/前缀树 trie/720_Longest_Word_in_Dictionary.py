'''
给出一个字符串数组 words 组成的一本英语词典。返回 words 中最长的一个单词，该单词是由 words 词典中其他单词逐步添加一个字母组成。

若其中有多个可行的答案，则返回答案中字典序最小的单词。若无答案，则返回空字符串。
'''

from typing import List
# 这个方案应该不是最优解，因为效率太低了
class TrieNode:
    def __init__(self):
        self.children = {}
        self.end_of_word = False  # 标记该节点是否为某个单词的结尾

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        """
        向前缀树中插入一个单词。
        """
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.end_of_word = True  # 标记单词结束

    def search(self, word: str) -> bool:
        """
        检查单词是否在前缀树中。
        """
        node = self.root
        for char in word:
            if char not in node.children or not node.children[char].end_of_word:
                return False
            node = node.children[char]
        return True

class Solution:
    def longestWord(self, words: List[str]) -> str:
        trie = Trie()
        # 先将所有单词插入前缀树
        for word in words:
            trie.insert(word)
        
        longest = ""
        # 遍历单词列表，查找满足条件的最长单词
        for word in sorted(words):  # 排序以确保字典序最小的优先
            if trie.search(word[:-1]) or len(word) == 1:  # 如果前缀存在或者单词长度为1
                if len(word) > len(longest):
                    longest = word
                elif len(word) == len(longest) and word < longest:
                    longest = word

        return longest

# 使用方法示例
sol = Solution()
result = sol.longestWord(["w", "wo", "wor", "worl", "world"])
print(result)  # 输出应该是 'world'
