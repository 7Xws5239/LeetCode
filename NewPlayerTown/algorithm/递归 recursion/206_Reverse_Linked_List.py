'''
给你单链表的头节点 head ，请你反转链表，并返回反转后的链表。
'''
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
# 这种递归方法的时间复杂度是 O(n)，因为它访问每个节点一次。空间复杂度也是 O(n)，主要是因为递归过程中的堆栈使用。递归方法虽然简洁，但在处理非常长的链表时需要注意可能的堆栈溢出问题。
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        递归地反转单链表。

        :param head: ListNode 单链表的头节点
        :return: ListNode 反转后的链表的头节点
        """
        # 递归终止条件：如果头节点为空或者链表只有一个节点，返回头节点
        if not head or not head.next:
            return head
        
        # 递归反转头节点之后的部分链表
        reversed_head = self.reverseList(head.next)
        
        # 将当前节点的下一个节点的next指针指向当前节点，完成反转
        head.next.next = head
        # 将当前节点的next指针置为空，避免成环
        head.next = None
        
        # 返回反转后的头节点，这是新的头节点
        return reversed_head

# 示例用法
# 创建链表 1 -> 2 -> 3 -> None
head = ListNode(1, ListNode(2, ListNode(3)))
sol = Solution()
new_head = sol.reverseList(head)  # 反转链表
# 打印反转后的链表
current = new_head
while current:
    print(current.val, end=" -> ")
    current = current.next
print("None")  # 输出: 3 -> 2 -> 1 -> None
