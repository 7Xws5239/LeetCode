'''
设计你的循环队列实现。 循环队列是一种线性数据结构，其操作表现基于 FIFO（先进先出）原则并且队尾被连接在队首之后以形成一个循环。它也被称为“环形缓冲器”。

循环队列的一个好处是我们可以利用这个队列之前用过的空间。在一个普通队列里，一旦一个队列满了，我们就不能插入下一个元素，即使在队列前面仍有空间。但是使用循环队列，我们能使用这些空间去存储新的值。

你的实现应该支持如下操作：

MyCircularQueue(k): 构造器，设置队列长度为 k 。
Front: 从队首获取元素。如果队列为空，返回 -1 。
Rear: 获取队尾元素。如果队列为空，返回 -1 。
enQueue(value): 向循环队列插入一个元素。如果成功插入则返回真。
deQueue(): 从循环队列中删除一个元素。如果成功删除则返回真。
isEmpty(): 检查循环队列是否为空。
isFull(): 检查循环队列是否已满。

示例：

MyCircularQueue circularQueue = new MyCircularQueue(3); // 设置长度为 3
circularQueue.enQueue(1);  // 返回 true
circularQueue.enQueue(2);  // 返回 true
circularQueue.enQueue(3);  // 返回 true
circularQueue.enQueue(4);  // 返回 false，队列已满
circularQueue.Rear();  // 返回 3
circularQueue.isFull();  // 返回 true
circularQueue.deQueue();  // 返回 true
circularQueue.enQueue(4);  // 返回 true
circularQueue.Rear();  // 返回 4
 

提示：

所有的值都在 0 至 1000 的范围内；
操作数将在 1 至 1000 的范围内；
请不要使用内置的队列库。
'''

# 定义循环队列类
class MyCircularQueue:
    
    # 循环队列的初始化方法
    def __init__(self, k: int):
        # self.k 存储队列的容量
        self.k = k
        # 以 None 填充初始化队列，队列的大小由 k 确定
        self.queue = [None] * k
        # 初始化头部和尾部指针为 -1，表示队列为空
        self.head = self.tail = -1

    # 向队列中插入一个元素的方法
    def enQueue(self, value: int) -> bool:
        # 检查队列是否已满，如果已满，返回 False 表示无法插入
        if self.isFull():
            return False
        # 如果队列为空，将头部指针设置为 0
        if self.isEmpty():
            self.head = 0
        # 循环方式将尾部指针向前移动 1 位置，并插入新的值
        self.tail = (self.tail + 1) % self.k
        self.queue[self.tail] = value
        # 返回 True 表示值已成功插入
        return True

    # 从队列中删除一个元素的方法
    def deQueue(self) -> bool:
        # 检查队列是否为空，如果为空，返回 False 表示没有元素可以删除
        if self.isEmpty():
            return False
        # 如果头部和尾部指针相等，表示队列中只有一个元素，将它们设置为 -1 表示队列为空
        if self.head == self.tail:
            self.head = self.tail = -1
        else:
            # 循环方式将头部指针向前移动 1 位置，有效地移除了队列前端的元素
            self.head = (self.head + 1) % self.k
        # 返回 True 表示成功执行了出队操作
        return True

    # 获取队列前端元素的方法
    def Front(self) -> int:
        # 如果队列为空，返回 -1；否则，返回头部指针处的值
        return -1 if self.isEmpty() else self.queue[self.head]

    # 获取队列尾端元素的方法
    def Rear(self) -> int:
        # 如果队列为空，返回 -1；否则，返回尾部指针处的值
        return -1 if self.isEmpty() else self.queue[self.tail]

    # 辅助方法，用于检查队列是否为空
    def isEmpty(self) -> bool:
        # 如果头部指针为 -1，则认为队列为空
        return self.head == -1

    # 辅助方法，用于检查队列是否已满
    def isFull(self) -> bool:
        # 如果向前移动尾部指针会使其等于头部指针，则认为队列已满
        return (self.tail + 1) % self.k == self.head




# Your MyCircularQueue object will be instantiated and called as such:
obj = MyCircularQueue(3) # 设置长度为3
param_1 = obj.enQueue(1) # 返回true
print(param_1)
param_1 = obj.enQueue(2) # 返回true
print(param_1)
param_1 = obj.enQueue(3) # 返回true
print(param_1)
param_1 = obj.enQueue(4) # 返回false，队列已满
print(param_1)
param_2 = obj.Rear() # 返回3
print(param_2)
param_3 = obj.isFull() # 返回true
print(param_3)
param_4 = obj.deQueue() # 返回true
print(param_4)
param_5 = obj.enQueue(4) # 返回true
print(param_5)
param_6 = obj.Rear() #返回4
print(param_6)