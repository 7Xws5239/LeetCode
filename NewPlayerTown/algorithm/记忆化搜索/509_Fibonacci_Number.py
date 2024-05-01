'''
斐波那契数 （通常用 F(n) 表示）形成的序列称为 斐波那契数列 。该数列由 0 和 1 开始，后面的每一项数字都是前面两项数字的和。也就是：

F(0) = 0，F(1) = 1
F(n) = F(n - 1) + F(n - 2)，其中 n > 1
给定 n ，请计算 F(n) 。
'''

class Solution:
    def fib(self, n: int) -> int:
        # 创建一个字典来存储已计算的斐波那契数值，以减少重复计算
        memo = {}
        
        def calculate_fib(k):
            # 如果k为0或1，直接返回k（因为F(0) = 0, F(1) = 1）
            if k <= 1:
                return k
            
            # 如果已经计算过这个值，则直接从memo中获取
            if k in memo:
                return memo[k]
            
            # 计算斐波那契数并存入memo以供后续使用
            memo[k] = calculate_fib(k - 1) + calculate_fib(k - 2)
            return memo[k]
        
        # 计算并返回F(n)
        return calculate_fib(n)

# 用例测试
sol = Solution()
print(sol.fib(10))  # 应该输出55
