'''
nums1 中数字 x 的 下一个更大元素 是指 x 在 nums2 中对应位置 右侧 的 第一个 比 x 大的元素。

给你两个 没有重复元素 的数组 nums1 和 nums2 ，下标从 0 开始计数，其中nums1 是 nums2 的子集。

对于每个 0 <= i < nums1.length ，找出满足 nums1[i] == nums2[j] 的下标 j ，并且在 nums2 确定 nums2[j] 的 下一个更大元素 。如果不存在下一个更大元素，那么本次查询的答案是 -1 。

返回一个长度为 nums1.length 的数组 ans 作为答案，满足 ans[i] 是如上所述的 下一个更大元素 。

 

示例 1：

输入：nums1 = [4,1,2], nums2 = [1,3,4,2].
输出：[-1,3,-1]
解释：nums1 中每个值的下一个更大元素如下所述：
- 4 ，用加粗斜体标识，nums2 = [1,3,4,2]。不存在下一个更大元素，所以答案是 -1 。
- 1 ，用加粗斜体标识，nums2 = [1,3,4,2]。下一个更大元素是 3 。
- 2 ，用加粗斜体标识，nums2 = [1,3,4,2]。不存在下一个更大元素，所以答案是 -1 。
示例 2：

输入：nums1 = [2,4], nums2 = [1,2,3,4].
输出：[3,-1]
解释：nums1 中每个值的下一个更大元素如下所述：
- 2 ，用加粗斜体标识，nums2 = [1,2,3,4]。下一个更大元素是 3 。
- 4 ，用加粗斜体标识，nums2 = [1,2,3,4]。不存在下一个更大元素，所以答案是 -1 。
 

提示：

1 <= nums1.length <= nums2.length <= 1000
0 <= nums1[i], nums2[i] <= 104
nums1和nums2中所有整数 互不相同
nums1 中的所有整数同样出现在 nums2 中
 

进阶：你可以设计一个时间复杂度为 O(nums1.length + nums2.length) 的解决方案吗？
'''
from typing import List
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # 初始化一个栈和一个哈希表用来存储nums2中每个元素的下一个更大元素
        stack, next_greater = [], {}
        
        # 遍历nums2，使用单调栈找出所有元素的下一个更大元素
        for num in nums2:
            # 当栈不为空且栈顶元素小于当前元素时，说明找到了栈顶元素的下一个更大元素
            while stack and stack[-1] < num:
                next_greater[stack.pop()] = num
            # 将当前元素压入栈中
            stack.append(num)
        
        # 对于栈中剩余的元素，它们没有下一个更大元素，因此对应的值为-1
        for num in stack:
            next_greater[num] = -1
        
        # 根据nums1中的元素顺序，从哈希表中找出对应的下一个更大元素
        result = [next_greater[num] for num in nums1]
        return result

# 创建Solution实例
solution = Solution()
# 测试示例
nums1 = [4,1,2]
nums2 = [1,3,4,2]
# 调用函数并打印结果
result = solution.nextGreaterElement(nums1, nums2)

