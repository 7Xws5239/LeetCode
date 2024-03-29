'''
写一个 RecentCounter 类来计算特定时间范围内最近的请求。

请你实现 RecentCounter 类：

RecentCounter() 初始化计数器，请求数为 0 。
int ping(int t) 在时间 t 添加一个新请求，其中 t 表示以毫秒为单位的某个时间，并返回过去 3000 毫秒内发生的所有请求数（包括新请求）。确切地说，返回在 [t-3000, t] 内发生的请求数。
保证 每次对 ping 的调用都使用比之前更大的 t 值。
'''
from collections import deque
class RecentCounter:
    def __init__(self) -> None:
        self.queue = deque() #我不确定我的理解对不对，这里可能不应该理解为点到queue，因为这里是一个定义，所以它的意思应该是拿到这个属性
                             #另外，这里的deque不是表示删除的意思，这是一个双端队列

    def ping(self,t):
        self.queue.append(t)

        while self.queue[0] < t-3000:
            self.queue.popleft()
        
        return len(self.queue)


obj = RecentCounter()
t1=1
t2=100
t3=3001
t4=3002
obj.ping(t1)
obj.ping(t2)
obj.ping(t3)
number_of_requests = obj.ping(t4)

print(number_of_requests)

