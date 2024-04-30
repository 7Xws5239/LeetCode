'''
给定一个列表 accounts，每个元素 accounts[i] 是一个字符串列表，其中第一个元素 accounts[i][0] 是 名称 (name)，其余元素是 emails 表示该账户的邮箱地址。

现在，我们想合并这些账户。如果两个账户都有一些共同的邮箱地址，则两个账户必定属于同一个人。请注意，即使两个账户具有相同的名称，它们也可能属于不同的人，因为人们可能具有相同的名称。一个人最初可以拥有任意数量的账户，但其所有账户都具有相同的名称。

合并账户后，按以下格式返回账户：每个账户的第一个元素是名称，其余元素是 按字符 ASCII 顺序排列 的邮箱地址。账户本身可以以 任意顺序 返回。
'''

from typing import List
from collections import defaultdict
# 这种方法不仅可以高效地处理账户合并问题，而且还可以确保在最终输出中没有重复的账户，且每个账户的邮箱都是有序的。
class UnionFind:
    def __init__(self):
        self.parent = {}
    
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  # 路径压缩
        return self.parent[x]
    
    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX != rootY:
            self.parent[rootX] = rootY
    
    def add(self, x):
        if x not in self.parent:
            self.parent[x] = x

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        """
        使用并查集合并具有共同邮箱的账户。

        :param accounts: List[List[str]] 账户列表，每个账户包括姓名和若干邮箱
        :return: List[List[str]] 合并后的账户列表
        """
        uf = UnionFind()
        email_to_name = {}
        email_to_root = {}
        
        # 第一步：构建并查集
        for account in accounts:
            name = account[0]
            first_email = account[1]
            for email in account[1:]:
                uf.add(email)
                email_to_name[email] = name
                uf.union(first_email, email)
        
        # 第二步：将每个邮箱映射到其根邮箱
        for email in uf.parent:
            root = uf.find(email)
            if root not in email_to_root:
                email_to_root[root] = []
            email_to_root[root].append(email)
        
        # 第三步：构建结果
        merged_accounts = []
        for emails in email_to_root.values():
            name = email_to_name[emails[0]]  # 使用第一个邮箱找到对应的名字
            merged_accounts.append([name] + sorted(emails))
        
        return merged_accounts

# 示例用法
sol = Solution()
accounts = [
    ["John", "johnsmith@mail.com", "john_newyork@mail.com"],
    ["John", "johnsmith@mail.com", "john00@mail.com"],
    ["Mary", "mary@mail.com"],
    ["John", "johnnybravo@mail.com"]
]
print(sol.accountsMerge(accounts))

'''
对于账户合并问题，最优解通常是使用并查集或深度优先搜索（DFS）方法，两者各有优势，具体哪个更优取决于实现细节和运行环境。

### 比较 DFS 和并查集：

1. **并查集：**
   - **优点：**高效处理大量的动态连接问题，特别适合频繁查询和合并操作的场景。并查集非常适用于管理和查询元素的组关系，尤其当涉及大量合并和路径压缩优化时。
   - **性能：**操作的均摊时间复杂度几乎是常数级别 \(O(\alpha(n))\)，\(\alpha\) 是阿克曼函数的反函数。

2. **深度优先搜索（DFS）：**
   - **优点：**实现简单，适合一次性处理静态数据，可以在构建一次图之后快速完成搜索。
   - **性能：**DFS的时间复杂度为 \(O(V + E)\)，其中 \(V\) 是顶点数，\(E\) 是边数。在账户合并问题中，每次DFS调用可以遍历一个完整的连通分量。

### 实际性能考量：

在大多数情况下，**并查集和DFS都可以非常快速地解决问题**，但具体哪个更快可能取决于以下因素：

- **数据结构优化**：并查集的优化（路径压缩和按秩合并）可能使其在具体实现上比未优化的DFS更快。
- **数据特性**：如果连通分量非常大或很分散，DFS可能会因为频繁的递归调用而稍显不利，尤其是在有栈溢出风险的环境中。相反，并查集几乎不受此影响。
- **实现细节**：例如，DFS需要构建图，并处理好递归调用；并查集需要有效管理节点的父引用和集合的合并。实现的优化水平直接影响最终性能。

### 推荐最优解：

在**大规模数据**处理和需要**高效动态处理**的情况下，**并查集通常是首选**，因为它提供了更可预测的性能和较低的管理开销。并查集是解决动态连通性问题的标准工具，特别适合于复杂或大规模的合并场景。

在小到中等规模的数据集，或者在实现简便性更为重要的场景下，**DFS也是一个非常好的选择**，尤其是如果你已经熟悉图遍历算法的实现。

在选择最优解时，考虑问题的具体需求和实际运行环境是关键。如果性能差异不大，选择最易于实现和维护的方法也是合理的。
'''

# 官方答案（速度明显快得多，也是用了并查集）：

'''
class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))

    def union(self, index1: int, index2: int):
        self.parent[self.find(index2)] = self.find(index1)

    def find(self, index: int) -> int:
        if self.parent[index] != index:
            self.parent[index] = self.find(self.parent[index])
        return self.parent[index]

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        emailToIndex = dict()
        emailToName = dict()

        for account in accounts:
            name = account[0]
            for email in account[1:]:
                if email not in emailToIndex:
                    emailToIndex[email] = len(emailToIndex)
                    emailToName[email] = name
        
        uf = UnionFind(len(emailToIndex))
        for account in accounts:
            firstIndex = emailToIndex[account[1]]
            for email in account[2:]:
                uf.union(firstIndex, emailToIndex[email])
        
        indexToEmails = collections.defaultdict(list)
        for email, index in emailToIndex.items():
            index = uf.find(index)
            indexToEmails[index].append(email)
        
        ans = list()
        for emails in indexToEmails.values():
            ans.append([emailToName[emails[0]]] + sorted(emails))
        return ans


'''