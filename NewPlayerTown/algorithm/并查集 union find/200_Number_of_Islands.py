'''
给你一个由 '1'（陆地）和 '0'（水）组成的的二维网格，请你计算网格中岛屿的数量。

岛屿总是被水包围，并且每座岛屿只能由水平方向和/或竖直方向上相邻的陆地连接形成。

此外，你可以假设该网格的四条边均被水包围。
'''

from typing import List
# 使用并查集解决岛屿问题是一种有效的方法，特别适用于大型数据，因为其操作几乎是常数时间的，这使得处理大型网格变得非常高效。
# 实际提交的时候这个问题用并查集的方法速度很慢
# 为什么leetcode提交的时候并查集耗时长的原因放在了最后

class UnionFind:
    def __init__(self, grid):
        self.count = 0
        self.parent = {}
        self.rank = {}
        rows, cols = len(grid), len(grid[0])
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1':
                    self.parent[(r, c)] = (r, c)
                    self.rank[(r, c)] = 0
                    self.count += 1
    
    def find(self, i):
        if self.parent[i] != i:
            self.parent[i] = self.find(self.parent[i])
        return self.parent[i]
    
    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX != rootY:
            if self.rank[rootX] > self.rank[rootY]:
                self.parent[rootY] = rootX
            elif self.rank[rootX] < self.rank[rootY]:
                self.parent[rootX] = rootY
            else:
                self.parent[rootY] = rootX
                self.rank[rootX] += 1
            self.count -= 1

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        """
        使用并查集计算网格中的岛屿数量。

        :param grid: List[List[str]] 二维网格
        :return: int 岛屿数量
        """
        if not grid or not grid[0]:
            return 0
        
        uf = UnionFind(grid)
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        rows, cols = len(grid), len(grid[0])

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1':
                    for dr, dc in directions:
                        nr, nc = r + dr, c + dc
                        if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == '1':
                            uf.union((r, c), (nr, nc))

        return uf.count

# 示例用法
sol = Solution()
grid = [
    ["1", "1", "0", "0", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "1", "0", "0"],
    ["0", "0", "0", "1", "1"]
]
print(sol.numIslands(grid))  # 输出: 3

'''
在实际应用中，尤其是在竞赛和在线评测平台如 LeetCode 上，你可能会发现并查集在处理岛屿数量问题时相比于 BFS 和 DFS 有更长的运行时间。这种现象可能由几个因素造成：

### 1. **操作成本**:
- **并查集** 操作涉及更多的逻辑层次，比如查找操作需要执行路径压缩，联合操作需要按秩合并。尽管这些操作都有助于保持结构尽量扁平，以提高效率，但在每个操作中涉及的步骤比单纯的访问和标记（如在 BFS 或 DFS 中）要多。因此，单次操作的时间复杂度虽然接近常数，但常数因子可能比较大。

### 2. **初始化开销**:
- **并查集** 需要初始化额外的数据结构（如每个节点的父节点数组和秩数组），这在开始时就有一定的时间和空间开销。

### 3. **局部性差**:
- 访问内存的局部性在现代计算机架构中对性能有显著影响。在 BFS 和 DFS 中，访问通常局限于相邻的内存位置（尤其是在处理连续的网格数据时）。而在并查集中，节点的父节点引用可能会跳跃到数组的不同部分，这可能导致缓存未命中率较高，影响性能。

### 4. **简单问题的复杂解法**:
- 对于简单的岛屿问题，BFS 和 DFS 提供了直接而有效的解决方案，这些方法直接利用了网格的物理结构。并查集虽然在理论上适合处理连通性问题，但其额外的复杂性在这种特定情况下可能是过度的。

### 5. **平台实现细节**:
- 不同在线平台的测试用例和底层硬件也会影响执行时间。例如，如果大多数测试用例包含的岛屿较少但网格很大，BFS 和 DFS 可能因为简单的访问和标记操作而具有优势。

### 结论:
在选择算法时，理解每种算法的工作原理及其与问题特性的匹配度非常重要。对于大多数标准的岛屿计数问题，DFS 和 BFS 的简单性和直接性使它们在实际应用中表现更好，特别是在标准测试平台上。并查集虽然在理论上很优雅，并适用于复杂的动态连通性问题，但可能不是解决所有类型的岛屿问题的最优选择。在选择解决方案时考虑问题的具体要求和实际环境是很重要的。
'''
