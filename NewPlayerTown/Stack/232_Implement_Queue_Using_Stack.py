'''
请你仅使用两个栈实现先入先出队列。队列应当支持一般队列支持的所有操作（push、pop、peek、empty）：

实现 MyQueue 类：

void push(int x) 将元素 x 推到队列的末尾
int pop() 从队列的开头移除并返回元素
int peek() 返回队列开头的元素
boolean empty() 如果队列为空，返回 true ；否则，返回 false
说明：

你 只能 使用标准的栈操作 —— 也就是只有 push to top, peek/pop from top, size, 和 is empty 操作是合法的。
你所使用的语言也许不支持栈。你可以使用 list 或者 deque（双端队列）来模拟一个栈，只要是标准的栈操作即可。
 

示例 1：

输入：
["MyQueue", "push", "push", "peek", "pop", "empty"]
[[], [1], [2], [], [], []]
输出：
[null, null, null, 1, 1, false]

解释：
MyQueue myQueue = new MyQueue();
myQueue.push(1); // queue is: [1]
myQueue.push(2); // queue is: [1, 2] (leftmost is front of the queue)
myQueue.peek(); // return 1
myQueue.pop(); // return 1, queue is [2]
myQueue.empty(); // return false
 

提示：

1 <= x <= 9
最多调用 100 次 push、pop、peek 和 empty
假设所有操作都是有效的 （例如，一个空的队列不会调用 pop 或者 peek 操作）
 

进阶：

你能否实现每个操作均摊时间复杂度为 O(1) 的队列？换句话说，执行 n 个操作的总时间复杂度为 O(n) ，即使其中一个操作可能花费较长时间。
'''

class MyQueue:
    def __init__(self):
        # 初始化两个栈，一个用于入队，一个用于出队
        self.in_stack = [] #请注意，这里的两个对象实际上都是列表，但是python的列表比较特殊，它是具有栈操作特性的。
        self.out_stack = []

    def push(self, x: int) -> None:
        # 入队操作，直接将元素压入in_stack栈
        self.in_stack.append(x)

    def pop(self) -> int:
        # 出队操作
        if not self.out_stack:
            # 如果out_stack为空，则将in_stack中的所有元素逆序压入out_stack中
            while self.in_stack:
                self.out_stack.append(self.in_stack.pop())
        # 返回并弹出out_stack栈顶元素，即队首元素
        return self.out_stack.pop()

    def peek(self) -> int:
        # 获取队首元素
        if not self.out_stack:
            # 如果out_stack为空，则将in_stack中的所有元素逆序压入out_stack中
            while self.in_stack:
                self.out_stack.append(self.in_stack.pop())
        # 返回out_stack栈顶元素，但不弹出，即队首元素
        return self.out_stack[-1] #这里的‘-1’是因为python中负数索引可以获取倒数的元素，这里的负一是倒数第一个元素的意思

    def empty(self) -> bool:
        # 判断队列是否为空
        # 当两个栈都为空时，队列为空
        return not self.in_stack and not self.out_stack

# # 创建队列实例
# queue = MyQueue()

# # 按示例操作队列
# operations = ["push", "push", "peek", "pop", "empty"]
# values = [[1], [2], [], [], []]
# results = []

# for op, value in zip(operations, values):
#     if op == "push":
#         queue.push(value[0])
#         results.append(None)
#     elif op == "pop":
#         results.append(queue.pop())
#     elif op == "peek":
#         results.append(queue.peek())
#     elif op == "empty":
#         results.append(queue.empty())


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()