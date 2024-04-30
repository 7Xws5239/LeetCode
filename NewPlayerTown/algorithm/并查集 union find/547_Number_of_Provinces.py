'''
有 n 个城市，其中一些彼此相连，另一些没有相连。如果城市 a 与城市 b 直接相连，且城市 b 与城市 c 直接相连，那么城市 a 与城市 c 间接相连。

省份 是一组直接或间接相连的城市，组内不含其他没有相连的城市。

给你一个 n x n 的矩阵 isConnected ，其中 isConnected[i][j] = 1 表示第 i 个城市和第 j 个城市直接相连，而 isConnected[i][j] = 0 表示二者不直接相连。

返回矩阵中 省份 的数量。
'''

from typing import List

class UnionFind:
    def __init__(self, size):
        self.root = [i for i in range(size)]
        self.rank = [1] * size
    
    def find(self, x):
        if self.root[x] != x:
            self.root[x] = self.find(self.root[x])  # 路径压缩
        return self.root[x]
    
    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        
        if rootX != rootY:
            if self.rank[rootX] > self.rank[rootY]:
                self.root[rootY] = rootX
            elif self.rank[rootX] < self.rank[rootY]:
                self.root[rootX] = rootY
            else:
                self.root[rootY] = rootX
                self.rank[rootX] += 1
    
    def count(self):
        root_set = set(self.find(x) for x in range(len(self.root)))
        return len(root_set)

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        """
        使用并查集计算矩阵中的省份数量。

        :param isConnected: List[List[int]] 城市间连接的矩阵
        :return: int 省份数量
        """
        if not isConnected:
            return 0
        
        n = len(isConnected)
        uf = UnionFind(n)
        
        for i in range(n):
            for j in range(i + 1, n):
                if isConnected[i][j] == 1:
                    uf.union(i, j)
        
        return uf.count()

# 示例用法
sol = Solution()
isConnected = [
    [1, 1, 0],
    [1, 1, 0],
    [0, 0, 1]
]
print(sol.findCircleNum(isConnected))  # 输出: 2
