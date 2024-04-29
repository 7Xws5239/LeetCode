'''
给你一个满足下述两条属性的 m x n 整数矩阵：

每行中的整数从左到右按非严格递增顺序排列。
每行的第一个整数大于前一行的最后一个整数。
给你一个整数 target ，如果 target 在矩阵中，返回 true ；否则，返回 false 。
'''

from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        """
        使用二分查找在一个特殊的矩阵中查找目标值。
        
        :param matrix: List[List[int]] 按照题目描述排列的矩阵
        :param target: int 需要查找的目标整数
        :return: bool 如果找到目标值返回 true，否则返回 false
        """
        if not matrix:
            return False
        
        # 获取矩阵的行数和列数
        m, n = len(matrix), len(matrix[0])
        
        # 将矩阵想象为一个展开后的排序数组进行二分查找
        left, right = 0, m * n - 1
        
        while left <= right:
            mid = (left + right) // 2
            # 将一维的索引 mid 转换成二维索引 (row, col)
            row = mid // n
            col = mid % n
            
            # 检查中间位置的值
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] < target:
                left = mid + 1
            else:
                right = mid - 1
        
        # 如果循环结束也没有找到 target
        return False

# 示例用法
sol = Solution()
matrix = [
    [1, 3, 5, 7],
    [10, 11, 16, 20],
    [23, 30, 34, 60]
]
target = 3
print(sol.searchMatrix(matrix, target))  # 输出: True

target = 13
print(sol.searchMatrix(matrix, target))  # 输出: False
