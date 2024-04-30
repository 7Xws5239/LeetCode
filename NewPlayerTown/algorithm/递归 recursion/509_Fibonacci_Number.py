'''
斐波那契数 （通常用 F(n) 表示）形成的序列称为 斐波那契数列 。该数列由 0 和 1 开始，后面的每一项数字都是前面两项数字的和。也就是：

F(0) = 0，F(1) = 1
F(n) = F(n - 1) + F(n - 2)，其中 n > 1
给定 n ，请计算 F(n) 。
'''
# 请注意这里的递归法效率是非常低的，复杂度在O(2的n)
class Solution:
    def fib(self, n: int) -> int:
        """
        使用递归计算第 n 个斐波那契数。

        :param n: int 要计算的斐波那契数列的位置
        :return: int 返回第 n 个斐波那契数
        """
        # 递归终止条件：当 n 为 0 或 1 时，直接返回 n
        if n <= 1:
            return n
        
        # 递归调用自身计算前两个斐波那契数的和
        return self.fib(n - 1) + self.fib(n - 2)

# 示例用法
sol = Solution()
print(sol.fib(10))  # 输出: 55
