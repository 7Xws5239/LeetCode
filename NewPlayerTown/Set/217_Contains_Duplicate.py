'''
给你一个整数数组 nums 。如果任一值在数组中出现 至少两次 ，返回 true ；如果数组中每个元素互不相同，返回 false 。
 

示例 1：

输入：nums = [1,2,3,1]
输出：true
示例 2：

输入：nums = [1,2,3,4]
输出：false
示例 3：

输入：nums = [1,1,1,3,3,4,3,2,4,2]
输出：true
 

提示：

1 <= nums.length <= 105
-109 <= nums[i] <= 109
'''

# 首先，我们需要导入类型提示功能，以便我们可以指定输入列表的类型。
from typing import List

# 定义Solution类
class Solution:
    # 定义containsDuplicate方法，该方法接受一个整数列表nums作为参数，并返回一个布尔值。
    def containsDuplicate(self, nums: List[int]) -> bool:
        # 创建一个空集合用于存储遍历过程中遇到的唯一元素。
        # 集合（Set）是一个无序的不重复元素序列，可以用来快速检查一个元素是否出现过。
        seen = set()
        
        # 遍历输入的整数列表。
        for num in nums:
            # 检查当前元素是否已经在之前出现过，即它是否已经在集合seen中。
            if num in seen:
                # 如果当前元素已经出现过，说明存在重复元素，因此返回True。
                return True
            # 如果当前元素未出现过，将其添加到集合seen中，以便记录这个元素已经遍历过。
            seen.add(num)
            
        # 如果遍历完成后没有找到任何重复的元素，返回False。
        return False

# 示例代码，如何使用上面定义的类和方法。
if __name__ == "__main__":
    # 创建Solution类的实例。
    solution = Solution()
    
    # 调用containsDuplicate方法并打印结果，以检查是否存在重复元素。
    print(solution.containsDuplicate([1,2,3,1]))  # 应该输出: True
    print(solution.containsDuplicate([1,2,3,4]))  # 应该输出: False
    print(solution.containsDuplicate([1,1,1,3,3,4,3,2,4,2]))  # 应该输出: True
