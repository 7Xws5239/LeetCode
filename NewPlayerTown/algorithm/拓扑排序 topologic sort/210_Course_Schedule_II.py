'''
现在你总共有 numCourses 门课需要选，记为 0 到 numCourses - 1。给你一个数组 prerequisites ，其中 prerequisites[i] = [ai, bi] ，表示在选修课程 ai 前 必须 先选修 bi 。

例如，想要学习课程 0 ，你需要先完成课程 1 ，我们用一个匹配来表示：[0,1] 。
返回你为了学完所有课程所安排的学习顺序。可能会有多个正确的顺序，你只要返回 任意一种 就可以了。如果不可能完成所有课程，返回 一个空数组 。
'''

from typing import List
from collections import deque

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # 构建图的邻接表和每个节点的入度表
        adjacency_list = [[] for _ in range(numCourses)]
        in_degree = [0] * numCourses
        
        # 构建图，并计算每个课程的入度
        for course, pre in prerequisites:
            adjacency_list[pre].append(course)
            in_degree[course] += 1
        
        # 初始化队列，包括所有入度为0的课程
        queue = deque([i for i in range(numCourses) if in_degree[i] == 0])
        
        # 存储拓扑排序的结果
        order = []
        
        # 进行拓扑排序
        while queue:
            course = queue.popleft()
            order.append(course)
            # 遍历所有依赖该课程的后续课程
            for next_course in adjacency_list[course]:
                in_degree[next_course] -= 1  # 减少入度
                if in_degree[next_course] == 0:  # 如果入度为0，加入队列
                    queue.append(next_course)
        
        # 检查是否所有课程都被排序
        if len(order) == numCourses:
            return order
        else:
            return []

# 使用方法示例
sol = Solution()
result = sol.findOrder(4, [[1,0],[2,0],[3,1],[3,2]])
print(result)  # 可能的输出：[0, 1, 2, 3]
