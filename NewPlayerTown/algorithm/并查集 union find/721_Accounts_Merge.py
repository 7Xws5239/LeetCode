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
