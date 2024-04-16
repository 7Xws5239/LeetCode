'''
不使用任何内建的哈希表库设计一个哈希集合（HashSet）。

实现 MyHashSet 类：

void add(key) 向哈希集合中插入值 key 。
bool contains(key) 返回哈希集合中是否存在这个值 key 。
void remove(key) 将给定值 key 从哈希集合中删除。如果哈希集合中没有这个值，什么也不做。
 
示例：

输入：
["MyHashSet", "add", "add", "contains", "contains", "add", "contains", "remove", "contains"]
[[], [1], [2], [1], [3], [2], [2], [2], [2]]
输出：
[null, null, null, true, false, null, true, null, false]

解释：
MyHashSet myHashSet = new MyHashSet();
myHashSet.add(1);      // set = [1]
myHashSet.add(2);      // set = [1, 2]
myHashSet.contains(1); // 返回 True
myHashSet.contains(3); // 返回 False ，（未找到）
myHashSet.add(2);      // set = [1, 2]
myHashSet.contains(2); // 返回 True
myHashSet.remove(2);   // set = [1]
myHashSet.contains(2); // 返回 False ，（已移除）
 

提示：

0 <= key <= 106
最多调用 104 次 add、remove 和 contains
'''

class ListNode:
    """
    定义一个链表节点，用于链地址法中每个桶的数据存储
    """
    def __init__(self, key, next=None):
        self.key = key
        self.next = next

class MyHashSet:
    def __init__(self):
        """
        初始化哈希集合。选择一个较小的初始桶数，以节省空间。
        """
        self.bucketCount = 769  # 使用质数作为桶的数量，可以帮助减少冲突
        self.buckets = [None] * self.bucketCount
        # 是在创建一个包含769个元素的列表，其中每个元素初始时都被设置为`None`。这意味着每个桶一开始都是空的，没有存储任何元素。

    def hash(self, key: int) -> int:
        """
        计算哈希值，决定键值对应的桶的索引。
        """
        return key % self.bucketCount

    def add(self, key: int) -> None:
        """
        向哈希集合中添加一个新键，如果这个键已经存在，则不做任何操作。
        """
        index = self.hash(key)
        # 如果桶是空的，直接添加新节点
        if not self.buckets[index]:
            self.buckets[index] = ListNode(key)
            return
        # 如果桶非空，遍历链表查找键，如果找不到则添加到链表末尾
        current = self.buckets[index]
        while True:
            if current.key == key:
                return  # 键已存在，不添加
            if not current.next:
                break
            current = current.next
        current.next = ListNode(key)  # 在链表末尾添加新节点

    def remove(self, key: int) -> None:
        """
        从哈希集合中删除指定的键，如果这个键不存在，则不做任何操作。
        """
        index = self.hash(key)
        current = self.buckets[index]
        prev = None
        while current:
            if current.key == key:
                if prev:
                    prev.next = current.next  # 删除非头节点
                else:
                    self.buckets[index] = current.next  # 删除头节点
                return
            prev = current
            current = current.next

    def contains(self, key: int) -> bool:
        """
        返回哈希集合中是否包含指定的键。
        """
        index = self.hash(key)
        current = self.buckets[index]
        while current:
            if current.key == key:
                return True
            current = current.next
        return False

# 示例代码
if __name__ == "__main__":
    myHashSet = MyHashSet()
    myHashSet.add(1)
    myHashSet.add(2)
    print(myHashSet.contains(1))  # 返回 True
    print(myHashSet.contains(3))  # 返回 False
    myHashSet.add(2)
    print(myHashSet.contains(2))  # 返回 True
    myHashSet.remove(2)
    print(myHashSet.contains(2))  # 返回 False


# class MyHashSet:
#     def __init__(self):
#         """
#         初始化哈希集合。使用一个大数组来存储元素，这里的大小是一个质数，可以减少哈希冲突。
#         使用None表示空位。
#         """
#         self.size = 1000001  # 选择一个大的空间以减少哈希冲突
#         self.table = [None] * self.size

#     def add(self, key: int) -> None:
#         """
#         向哈希集合中添加一个元素。通过计算哈希值来决定元素存放的位置。
#         如果该位置已被占用，则线性探测下一个位置。
#         """
#         index = key % self.size  # 计算哈希值
#         while self.table[index] is not None:  # 线性探测解决冲突
#             if self.table[index] == key:  # 如果元素已存在，则不需要添加
#                 return
#             index = (index + 1) % self.size  # 探测下一个位置
#         self.table[index] = key  # 在找到的空位置插入key

#     def remove(self, key: int) -> None:
#         """
#         从哈希集合中删除一个元素。首先找到元素的位置，然后将其删除。
#         """
#         index = key % self.size  # 计算哈希值
#         while self.table[index] is not None:  # 查找元素
#             if self.table[index] == key:  # 找到元素
#                 self.table[index] = None  # 删除元素
#                 return
#             index = (index + 1) % self.size  # 探测下一个位置

#     def contains(self, key: int) -> bool:
#         """
#         检查哈希集合中是否存在一个元素。通过哈希值定位元素位置，然后线性探测直到找到该元素或遇到一个空位。
#         """
#         index = key % self.size  # 计算哈希值
#         while self.table[index] is not None:  # 线性探测
#             if self.table[index] == key:  # 如果找到元素
#                 return True
#             index = (index + 1) % self.size  # 探测下一个位置
#         return False  # 未找到元素

# # 示例代码
# # 这部分是用于测试上面定义的MyHashSet类的功能
# if __name__ == "__main__":
#     myHashSet = MyHashSet()
#     myHashSet.add(1)
#     myHashSet.add(2)
#     print(myHashSet.contains(1))  # 返回 True
#     print(myHashSet.contains(3))  # 返回 False
#     myHashSet.add(2)
#     print(myHashSet.contains(2))  # 返回 True
#     myHashSet.remove(2)
#     print(myHashSet.contains(2))  # 返回 False




# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)