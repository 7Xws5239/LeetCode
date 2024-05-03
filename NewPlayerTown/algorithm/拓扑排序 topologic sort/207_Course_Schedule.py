'''
你这个学期必须选修 numCourses 门课程，记为 0 到 numCourses - 1 。

在选修某些课程之前需要一些先修课程。 先修课程按数组 prerequisites 给出，其中 prerequisites[i] = [ai, bi] ，表示如果要学习课程 ai 则 必须 先学习课程  bi 。

例如，先修课程对 [0, 1] 表示：想要学习课程 0 ，你需要先完成课程 1 。
请你判断是否可能完成所有课程的学习？如果可以，返回 true ；否则，返回 false 。
'''
# 拓扑排序可以帮助我们判断有向图中是否存在环，因为如果存在环，则无法完成所有课程的学习。
from typing import List
from collections import deque

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # 构建图的邻接表和入度数组
        adjacency_list = [[] for _ in range(numCourses)]
        in_degree = [0] * numCourses
        
        # 构建图，并计算每个节点的入度
        for dest, src in prerequisites:
            adjacency_list[src].append(dest)
            in_degree[dest] += 1
        
        # 使用队列实现拓扑排序
        queue = deque()
        
        # 所有入度为0的节点入队
        for i in range(numCourses):
            if in_degree[i] == 0:
                queue.append(i)
        
        # 已访问（已完成）的课程数
        visited_courses = 0
        
        # 拓扑排序处理
        while queue:
            course = queue.popleft()
            visited_courses += 1  # 该课程已完成
            
            # 对当前课程的所有邻接节点（依赖当前课程的课程），减少入度
            for neighbor in adjacency_list[course]:
                in_degree[neighbor] -= 1
                # 如果邻接节点的入度变为0，则入队
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)
        
        # 如果完成的课程数量等于课程总数，返回True
        return visited_courses == numCourses

# 使用方法示例
sol = Solution()
result = sol.canFinish(2, [[1, 0]])
print(result)  # 输出应该是 True
