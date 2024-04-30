'''
给定二叉搜索树的根结点 root，返回值位于范围 [low, high] 之间的所有结点的值的和。
'''

# 首先定义二叉树节点的结构
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import Optional

class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        """
        使用深度优先搜索计算二叉搜索树中给定范围内所有节点的值的和。

        :param root: Optional[TreeNode] 二叉搜索树的根节点
        :param low: int 范围的下界
        :param high: int 范围的上界
        :return: int 范围内所有节点的值的和
        """
        # 初始化结果变量
        self.sum = 0
        
        def dfs(node):
            """
            深度优先搜索辅助函数。

            :param node: TreeNode 当前访问的节点
            """
            if node is not None:
                # 如果当前节点的值在[low, high]范围内，将其值加到sum中
                if low <= node.val <= high:
                    self.sum += node.val
                # 如果当前节点的值大于low，继续搜索左子树
                if node.val > low:
                    dfs(node.left)
                # 如果当前节点的值小于high，继续搜索右子树
                if node.val < high:
                    dfs(node.right)
        
        # 从根节点开始深度优先搜索
        dfs(root)
        return self.sum

# 示例用法
# 构建一个简单的二叉搜索树
#         10
#        /  \
#       5   15
#      / \    \
#     3   7   18
root = TreeNode(10)
root.left = TreeNode(5, TreeNode(3), TreeNode(7))
root.right = TreeNode(15, None, TreeNode(18))

sol = Solution()
print(sol.rangeSumBST(root, 7, 15))  # 输出: 32
