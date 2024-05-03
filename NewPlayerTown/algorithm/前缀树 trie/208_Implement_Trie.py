'''
Trie（发音类似 "try"）或者说 前缀树 是一种树形数据结构，用于高效地存储和检索字符串数据集中的键。这一数据结构有相当多的应用情景，例如自动补完和拼写检查。

请你实现 Trie 类：

Trie() 初始化前缀树对象。
void insert(String word) 向前缀树中插入字符串 word 。
boolean search(String word) 如果字符串 word 在前缀树中，返回 true（即，在检索之前已经插入）；否则，返回 false 。
boolean startsWith(String prefix) 如果之前已经插入的字符串 word 的前缀之一为 prefix ，返回 true ；否则，返回 false 。
'''
# 这个实现中，Trie类使用一个字典children来存储子节点，每个节点都是一个Trie对象。isEndOfWord属性用来标记节点是否为某个单词的结尾。通过递归的方式，我们可以有效地插入、搜索以及查找具有特定前缀的字符串。
class Trie:
    def __init__(self):
        """
        初始化前缀树对象。
        """
        self.children = {}  # 用来存储子节点（即下一个字符）
        self.isEndOfWord = False  # 标记是否为某个单词的结尾

    def insert(self, word: str) -> None:
        """
        向前缀树中插入一个字符串。
        """
        current = self  # 从根节点开始
        for char in word:  # 遍历单词中的每一个字符
            if char not in current.children:  # 如果字符不在当前节点的子节点中
                current.children[char] = Trie()  # 创建一个新的Trie节点作为子节点
            current = current.children[char]  # 移动到该子节点
        current.isEndOfWord = True  # 完成插入后，标记单词结束的节点

    def search(self, word: str) -> bool:
        """
        搜索前缀树中是否存在字符串word。
        """
        current = self  # 从根节点开始
        for char in word:  # 遍历单词中的每一个字符
            if char not in current.children:  # 如果字符不在当前节点的子节点中
                return False  # 说明单词不存在于前缀树中
            current = current.children[char]  # 移动到子节点
        return current.isEndOfWord  # 返回是否找到完整的单词

    def startsWith(self, prefix: str) -> bool:
        """
        检查是否有单词以该前缀开始。
        """
        current = self  # 从根节点开始
        for char in prefix:  # 遍历前缀中的每一个字符
            if char not in current.children:  # 如果字符不在当前节点的子节点中
                return False  # 说明没有单词以这个前缀开始
            current = current.children[char]  # 移动到子节点
        return True  # 如果所有字符都找到了，说明有单词以这个前缀开始

# 如何使用前缀树:
# obj = Trie()
# obj.insert("word")
# param_2 = obj.search("word")
# param_3 = obj.startsWith("wo")
