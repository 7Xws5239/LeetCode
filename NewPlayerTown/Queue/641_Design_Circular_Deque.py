'''
设计实现双端队列。

实现 MyCircularDeque 类:

MyCircularDeque(int k) ：构造函数,双端队列最大为 k 。
boolean insertFront()：将一个元素添加到双端队列头部。 如果操作成功返回 true ，否则返回 false 。
boolean insertLast() ：将一个元素添加到双端队列尾部。如果操作成功返回 true ，否则返回 false 。
boolean deleteFront() ：从双端队列头部删除一个元素。 如果操作成功返回 true ，否则返回 false 。
boolean deleteLast() ：从双端队列尾部删除一个元素。如果操作成功返回 true ，否则返回 false 。
int getFront() )：从双端队列头部获得一个元素。如果双端队列为空，返回 -1 。
int getRear() ：获得双端队列的最后一个元素。 如果双端队列为空，返回 -1 。
boolean isEmpty() ：若双端队列为空，则返回 true ，否则返回 false  。
boolean isFull() ：若双端队列满了，则返回 true ，否则返回 false 。
'''

class MyCircularDeque:
    # 初始化双端队列
    def __init__(self, k: int):
        self.k = k  # 双端队列的最大容量
        self.queue = [None] * k  # 用列表表示双端队列，初始状态下全部填充为None
        self.head = self.tail = -1  # 初始化头部和尾部指针为-1，表示队列为空

    # 在双端队列前端添加元素
    def insertFront(self, value: int) -> bool:
        if self.isFull():  # 检查队列是否已满
            return False
        if self.isEmpty():  # 如果队列为空，则同时设置头部和尾部指针指向0
            self.head = self.tail = 0
        else:
            # 队列非空时，头部指针向前移动一位（循环移动）
            self.head = (self.head - 1 + self.k) % self.k
        self.queue[self.head] = value  # 在头部位置插入新元素
        return True

    # 在双端队列尾部添加元素
    def insertLast(self, value: int) -> bool:
        if self.isFull():  # 检查队列是否已满
            return False
        if self.isEmpty():  # 如果队列为空，则同时设置头部和尾部指针指向0
            self.head = self.tail = 0
        else:
            # 队列非空时，尾部指针向后移动一位（循环移动）
            self.tail = (self.tail + 1) % self.k
        self.queue[self.tail] = value  # 在尾部位置插入新元素
        return True

    # 从双端队列头部删除元素
    def deleteFront(self) -> bool:
        if self.isEmpty():  # 检查队列是否为空
            return False
        if self.head == self.tail:  # 队列只有一个元素时，删除后队列变为空
            self.head = self.tail = -1
        else:
            # 头部指针向后移动一位（循环移动）
            self.head = (self.head + 1) % self.k
        return True

    # 从双端队列尾部删除元素
    def deleteLast(self) -> bool:
        if self.isEmpty():  # 检查队列是否为空
            return False
        if self.head == self.tail:  # 队列只有一个元素时，删除后队列变为空
            self.head = self.tail = -1
        else:
            # 尾部指针向前移动一位（循环移动）
            self.tail = (self.tail - 1 + self.k) % self.k
        return True

    # 获取双端队列头部元素
    def getFront(self) -> int:
        if self.isEmpty():  # 检查队列是否为空
            return -1
        return self.queue[self.head]  # 返回头部元素

    # 获取双端队列尾部元素
    def getRear(self) -> int:
        if self.isEmpty():  # 检查队列是否为空
            return -1
        return self.queue[self.tail]  # 返回尾部元素

    # 检查双端队列是否为空
    def isEmpty(self) -> bool:
        return self.head == -1  # 头部指针为-1时表示队列为空

    # 检查双端队列是否已满
    def isFull(self) -> bool:
        # 如果头部位于尾部的下一个位置（循环考虑），则表示队列已满
        return (self.tail + 1) % self.k == self.head
