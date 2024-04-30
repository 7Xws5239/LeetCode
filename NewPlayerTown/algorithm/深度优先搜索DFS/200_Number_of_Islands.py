'''
给你一个由 '1'（陆地）和 '0'（水）组成的的二维网格，请你计算网格中岛屿的数量。

岛屿总是被水包围，并且每座岛屿只能由水平方向和/或竖直方向上相邻的陆地连接形成。

此外，你可以假设该网格的四条边均被水包围。
'''

from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        """
        使用深度优先搜索计算二维网格中岛屿的数量。

        :param grid: List[List[str]] 二维网格，由 '1'（陆地）和 '0'（水）组成
        :return: int 岛屿的数量
        """
        if not grid:
            return 0
        
        rows, cols = len(grid), len(grid[0])
        island_count = 0
        
        def dfs(r, c):
            """
            深度优先搜索辅助函数，用于标记与当前陆地相连的所有陆地为已访问。

            :param r: int 当前行的索引
            :param c: int 当前列的索引
            """
            if r < 0 or c < 0 or r >= rows or c >= cols or grid[r][c] == '0':
                return
            grid[r][c] = '0'  # 将当前陆地标记为水，避免重复访问
            # 检查四个方向的相邻单元格
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)
        
        # 遍历网格中的每个单元格
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1':  # 发现一个未被访问的岛屿
                    dfs(r, c)  # 通过DFS标记所有相连的陆地
                    island_count += 1  # 完成一个岛屿的探索后岛屿计数加一
        
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
