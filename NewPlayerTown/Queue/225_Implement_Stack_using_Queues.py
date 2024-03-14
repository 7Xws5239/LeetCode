'''
请你仅使用两个队列实现一个后入先出（LIFO）的栈，并支持普通栈的全部四种操作（push、top、pop 和 empty）。

实现 MyStack 类：

void push(int x) 将元素 x 压入栈顶。
int pop() 移除并返回栈顶元素。
int top() 返回栈顶元素。
boolean empty() 如果栈是空的，返回 true ；否则，返回 false 。
 

注意：

你只能使用队列的标准操作 —— 也就是 push to back、peek/pop from front、size 和 is empty 这些操作。
你所使用的语言也许不支持队列。 你可以使用 list （列表）或者 deque（双端队列）来模拟一个队列 , 只要是标准的队列操作即可。
'''

from collections import deque

class MyStack:
    def __init__(self):
        self.queue1 = deque()
        self.queue2 = deque()

    def push(self, x: int) -> None:
        # 将元素x加入到queue1中
        self.queue1.append(x)
        # 确保所有先前的元素都在x之后，以模拟栈的后入先出特性
        while self.queue2:
            self.queue1.append(self.queue2.popleft())
        # 交换queue1和queue2，使得queue1始终为空，queue2用于存储栈的所有元素
        self.queue1, self.queue2 = self.queue2, self.queue1

    def pop(self) -> int:
        # 从queue2中移除并返回最前端的元素，即最后插入的元素
        return self.queue2.popleft()

    def top(self) -> int:
        # 返回queue2最前端的元素，即最后插入的元素
        return self.queue2[0]

    def empty(self) -> bool:
        # 如果queue2为空，则栈为空
        return not self.queue2

ms = MyStack()
result = ms.empty()
ms.push(1)
ms.push(2)
ms.push(3)
ms.push(4)