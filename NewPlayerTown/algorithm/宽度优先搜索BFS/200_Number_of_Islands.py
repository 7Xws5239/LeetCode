'''
给你一个由 '1'（陆地）和 '0'（水）组成的的二维网格，请你计算网格中岛屿的数量。

岛屿总是被水包围，并且每座岛屿只能由水平方向和/或竖直方向上相邻的陆地连接形成。

此外，你可以假设该网格的四条边均被水包围。
'''

from typing import List
from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        """
        使用宽度优先搜索计算二维网格中岛屿的数量。

        :param grid: List[List[str]] 二维网格，由 '1'（陆地）和 '0'（水）组成
        :return: int 岛屿的数量
        """
        if not grid:
            return 0

        rows, cols = len(grid), len(grid[0])
        island_count = 0
        visited = set()

        def bfs(r, c):
            """
            使用宽度优先搜索从给定单元格开始探索所有相连的陆地。

            :param r: int 起始单元格的行索引
            :param c: int 起始单元格的列索引
            """
            queue = deque([(r, c)])
            visited.add((r, c))
            directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
            while queue:
                row, col = queue.popleft()
                for dr, dc in directions:
                    nr, nc = row + dr, col + dc
                    if (0 <= nr < rows and 0 <= nc < cols and
                            grid[nr][nc] == '1' and (nr, nc) not in visited):
                        queue.append((nr, nc))
                        visited.add((nr, nc))

        # 遍历网格中的每个单元格
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1' and (r, c) not in visited:
                    bfs(r, c)
                    island_count += 1  # 每完成一次BFS，岛屿数量增加1

        return island_count

# 示例用法
sol = Solution()
grid = [
    ["1", "1", "0", "0", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "1", "0", "0"],
    ["0", "0", "0", "1", "1"]
]
print(sol.numIslands(grid))  # 输出: 3
