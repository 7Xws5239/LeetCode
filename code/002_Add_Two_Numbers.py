'''
给你两个 非空 的链表，表示两个非负的整数。它们每位数字都是按照 逆序 的方式存储的，并且每个节点只能存储 一位 数字。

请你将两个数相加，并以相同形式返回一个表示和的链表。

你可以假设除了数字 0 之外，这两个数都不会以 0 开头。
'''

# # Definition for singly-linked list.
# from typing import Optional
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
    
#     ###################################      
#     def __str__(self): # 用于检查NodeList内容
#         return str(self.val)
# class Solution:
#     def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]: # 这里的optional如果找不到的原因：没有从typing导入
#         print()

#     ###################################    
#     def printList(self, node: Optional[ListNode]): # 用于检查NodeList内容
#         values = []
#         while node:
#             values.append(str(node.val))
#             node = node.next
#         return '->'.join(values)

# L1 = ListNode(2)
# L1.next = ListNode(4)
# L1.next.next = ListNode(3)


# L2 = ListNode(5)
# L2.next = ListNode(6)
# L2.next.next = ListNode(4)


# # 创建 Solution 实例并打印链表
# sol = Solution()
# print("L1:", sol.printList(L1))
# print("L2:", sol.printList(L2))


#---------------------------------------正确写法（迭代法）-------------------
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        total = 0
        next1 = 0
        dummy = ListNode()
        cur = dummy
        while(l1 != None and l2 != None):
            total = l1.val + l2.val + next1
            cur.next = ListNode(total % 10)
            next1 = total // 10
            cur = cur.next
            l1 = l1.next
            l2 = l2.next
        while l1 != None:
            total = l1.val + next1
            cur.next = ListNode(total % 10)
            next1 = total // 10
            cur = cur.next
            l1 = l1.next
        while l2 != None:
            total = l2.val + next1
            cur.next = ListNode(total % 10)
            next1 = total // 10
            cur = cur.next
            l2 = l2.next
        if next1 != 0:
            cur.next = ListNode(next1)
        return dummy.next
#---------------------------------------正确写法-------------------

#---------------------------------------正确写法（递归法）-------------------
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        total = l1.val + l2.val
        next1 = total // 10
        res = ListNode(total % 10)
        if (l1.next or l2.next or next1):
            l1 = l1.next if l1.next else ListNode(0)
            l2 = l2.next if l2.next else ListNode(0)
            l1.val += next1
            res.next = self.addTwoNumbers(l1,l2)
        return res



#---------------------------------------正确写法-------------------