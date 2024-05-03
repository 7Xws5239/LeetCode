'''
给你一个链表的头节点 head ，判断链表中是否有环。

如果链表中有某个节点，可以通过连续跟踪 next 指针再次到达，则链表中存在环。 
为了表示给定链表中的环，评测系统内部使用整数 pos 来表示链表尾连接到链表中的位置（索引从 0 开始）。注意：pos 不作为参数进行传递 。
仅仅是为了标识链表的实际情况。

如果链表中存在环 ，则返回 true 。 否则，返回 false 。
'''

from typing import Optional
# 定义单链表的节点类 #在LeetCode提交这块的ListNode定义要注释掉，否则提交得到的运行速度很慢。（连这句注释都要删除掉再提交才行。）
class ListNode:
    def __init__(self, x):
        self.val = x  # 节点存储的数据
        self.next = None  # 指向下一个节点的指针，初始化为 None

# 定义解决方案类
class Solution:
    # 方法定义，用于检测链表是否有环
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # 如果链表为空或只有一个节点，直接返回 False，因为至少需要两个节点才可能形成环
        if not head or not head.next:
            return False
        
        # 初始化两个指针，慢指针指向头节点，快指针指向头节点的下一个节点
        slow = head
        fast = head.next
        
        # 使用循环来移动快慢指针，直到它们相遇或快指针指向链表尾部
        while slow != fast:
            # 如果快指针或其下一个节点为空，表示到达链表尾部，没有环，返回 False
            if not fast or not fast.next:
                return False
            # 慢指针每次移动一个节点
            slow = slow.next
            # 快指针每次移动两个节点
            fast = fast.next.next
        
        # 如果快指针追上慢指针（两指针相遇），表示链表中存在环，返回 True
        return True

# 创建链表的几个节点
node1 = ListNode(3)
node2 = ListNode(2)
node3 = ListNode(0)
node4 = ListNode(-4)
# 将节点链接成链表
node1.next = node2
node2.next = node3
node3.next = node4
# 创建一个环，将链表最后一个节点的 next 指向 node2，形成环
node4.next = node2

# 创建解决方案对象
solution = Solution()
# 调用 hasCycle 方法检测链表是否有环，并打印结果
print(solution.hasCycle(node1))  # 输出: True，因为有环
