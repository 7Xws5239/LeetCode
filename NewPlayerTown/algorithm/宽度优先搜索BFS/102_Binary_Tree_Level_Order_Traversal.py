'''
给你二叉树的根节点 root ，返回其节点值的 层序遍历 。 （即逐层地，从左到右访问所有节点）。
'''

from typing import List, Optional
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        """
        使用宽度优先搜索进行二叉树的层序遍历。

        :param root: Optional[TreeNode] 二叉树的根节点
        :return: List[List[int]] 按层序返回节点的值
        """
        if not root:
            return []

        result = []
        queue = deque([root])  # 使用deque作为队列，初始化包含根节点

        while queue:
            level_size = len(queue)  # 当前层的节点数
            current_level = []  # 存储当前层的节点值

            for _ in range(level_size):
                node = queue.popleft()  # 从队列中取出当前节点
                current_level.append(node.val)  # 将当前节点的值添加到当前层的列表中
                
                # 如果当前节点有左子节点，将其加入队列
                if node.left:
                    queue.append(node.left)
                # 如果当前节点有右子节点，将其加入队列
                if node.right:
                    queue.append(node.right)
            
            result.append(current_level)  # 将当前层的结果添加到总结果列表中

        return result

# 示例用法
# 构建一个简单的二叉树
#         3
#        / \
#       9  20
#         /  \
#        15   7
root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20, TreeNode(15), TreeNode(7))

sol = Solution()
print(sol.levelOrder(root))  # 输出: [[3], [9, 20], [15, 7]]
