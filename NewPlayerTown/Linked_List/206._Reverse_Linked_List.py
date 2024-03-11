'''
给你单链表的头节点 head ，请你反转链表，并返回反转后的链表。
'''

from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
      
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
arr = [1,2,3,4,5,6]
head = create_list(arr)
print("Original List:")
print_list(head)


class Solution:
    def reverse_LinkedList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        current = head
        while current:
            next_temp = current.next
            current.next = prev
            prev = current
            current = next_temp
        return prev

# 使用 reverse_LinkedList
solution = Solution()
new_head = solution.reverse_LinkedList(head)

# 打印结果
print_list(new_head)          