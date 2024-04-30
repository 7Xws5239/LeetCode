'''
给定一个二叉树的 root ，返回 最长的路径的长度 ，这个路径中的 每个节点具有相同值 。 这条路径可以经过也可以不经过根节点。

两个节点之间的路径长度 由它们之间的边数表示。
'''
from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        """
        使用递归方法计算二叉树中最长的同值路径长度。
        
        :param root: TreeNode 二叉树的根节点
        :return: int 最长同值路径的长度
        """
        self.ans = 0  # 初始化最长路径长度为0

        def dfs(node):
            if not node:
                return 0

            # 递归计算左子树和右子树的同值路径长度
            left_length = dfs(node.left)
            right_length = dfs(node.right)

            # 初始化从当前节点向左和向右的同值路径长度
            left_univalue_length = 0
            right_univalue_length = 0
            
            # 如果左子节点存在且与当前节点值相同，则更新左侧同值路径长度
            if node.left and node.left.val == node.val:
                left_univalue_length = left_length + 1
            
            # 如果右子节点存在且与当前节点值相同，则更新右侧同值路径长度
            if node.right and node.right.val == node.val:
                right_univalue_length = right_length + 1
            
            # 更新全局最长同值路径长度
            self.ans = max(self.ans, left_univalue_length + right_univalue_length)
            
            # 返回以当前节点为起点的最长同值路径长度给上层节点
            return max(left_univalue_length, right_univalue_length)

        dfs(root)
        return self.ans

# 示例用法
sol = Solution()
# 构造二叉树，例如：
#     1
#    / \
#   4   5
#  / \
# 4   4
root = TreeNode(1)
root.left = TreeNode(4)
root.right = TreeNode(5)
root.left.left = TreeNode(4)
root.left.right = TreeNode(4)
print(sol.longestUnivaluePath(root))  # 输出: 2 (两个连续的4构成的路径)
