'''
给你一个链表的头节点 head 和一个整数 val ，请你删除链表中所有满足 Node.val == val 的节点，并返回 新的头节点 。
'''

# Definition for singly-linked list.
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        # 创建一个虚拟头节点，并让它指向实际的头节点
        dummy = ListNode(0)
        dummy.next = head

        # 初始化当前节点为虚拟头节点
        current = dummy

        # 遍历链表
        while current.next is not None:
            if current.next.val == val:
                # 删除节点：跳过当前节点
                current.next = current.next.next
            else:
                # 移动到下一个节点
                current = current.next

        # 返回新的头节点（跳过虚拟头节点）
        return dummy.next
                            

# 辅助函数：创建链表
def create_list(arr):
    head = ListNode(arr[0])
    current = head
    for value in arr[1:]:
        current.next = ListNode(value)
        current = current.next
    return head

# 辅助函数：打印链表
def print_list(node):
    while node:
        print(node.val, end=" -> ")
        node = node.next
    print("None")

# 创建链表
arr = [1, 2, 6, 3, 4, 5, 6]
head = create_list(arr)
print("Original List:")
print_list(head)

# 使用 removeElements
solution = Solution()
val_to_remove = 6
new_head = solution.removeElements(head, val_to_remove)

# 打印结果
print(f"List after removing {val_to_remove}:")
print_list(new_head)                            