'''
给定数组 people 。people[i]表示第 i 个人的体重 ，船的数量不限，每艘船可以承载的最大重量为 limit。

每艘船最多可同时载两人，但条件是这些人的重量之和最多为 limit。

返回 承载所有人所需的最小船数 。
'''

from typing import List

class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        """
        使用排序和双指针技术来确定最小需要的船只数，以在不超过载重限制的前提下尽可能地少使用船只。

        :param people: List[int] 表示每个人的体重
        :param limit: int 每艘船的最大承载重量
        :return: int 所需的最小船数
        """
        # 对人员根据体重进行排序
        people.sort()
        
        # 初始化左右指针
        left, right = 0, len(people) - 1
        # 初始化所需的船只数量
        boats = 0
        
        # 使用双指针从两端开始，尽量将最重的人与最轻的人配对
        while left <= right:
            # 如果最轻的人和最重的人的体重和小于等于限制，则两人可以同乘一艘船
            if people[left] + people[right] <= limit:
                left += 1  # 左指针向右移动，表示这个人已被安排上船
            # 无论是否配对成功，最重的人都必须上船
            right -= 1  # 右指针向左移动，表示这个人已被安排上船
            # 每进行一次操作，就需要一艘新的船
            boats += 1
        
        return boats

# 示例用法
sol = Solution()
people = [3, 5, 3, 4]
limit = 5
print(sol.numRescueBoats(people, limit))  # 输出应该为 4，因为每个人都不能与别人一起乘坐一艘船
