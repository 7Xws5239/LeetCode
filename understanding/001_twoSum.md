```python
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in hash_map:
                return [hash_map[complement], i]
            hash_map[num] = i
```            

当然，我很乐意详细解释这种使用哈希表的解决方案。这种方法是解决“两数之和”问题的高效方式。让我们一步一步来分析：

### 基本思想：
这个方案的核心思想是利用哈希表（也称为字典在Python中）来降低查找时间。在暴力解法中，我们对每个元素检查整个数组以找到其配对元素，这需要 O(n²) 的时间复杂度。而在这个方法中，我们只需要 O(n) 的时间复杂度，因为哈希表（字典）的查找时间几乎是常数级的。

### 代码解析：

1. **初始化哈希表**：
   ```python
   hash_map = {}
   ```
   我们创建一个空的哈希表（字典）来存储遍历过程中遇到的数字及其在数组中的索引。

2. **遍历数组**：
   ```python
   for i, num in enumerate(nums):
   ```
   使用 `enumerate` 函数遍历数组。`enumerate` 会同时返回每个元素的索引（`i`）和值（`num`）。

3. **计算补数并检查**：
   ```python
   complement = target - num
   if complement in hash_map:
       return [hash_map[complement], i]
   ```
   对于每个元素，我们计算 `target - num`（即补数），然后检查这个补数是否已经在我们的哈希表中。如果是，说明我们找到了一对数字，它们的和为 `target`。此时，我们返回这两个数字的索引：哈希表中补数的索引和当前数字的索引。

4. **添加元素到哈希表**：
   ```python
   hash_map[num] = i
   ```
   如果补数不在哈希表中，我们将当前元素及其索引添加到哈希表中。这样，如果后面的某个元素的补数是这个元素，我们就可以直接在哈希表中找到它。

### 为什么这种方法有效：
- **时间效率**：查找哈希表中是否存在一个键（本例中为补数）的时间复杂度接近 O(1)，所以整体算法的时间复杂度为 O(n)。
- **空间换时间**：我们使用额外的空间（哈希表）来存储信息，从而大大减少了查找时间。

这种方法只需要遍历数组一次，每次遍历中只进行常数时间级别的工作（计算补数和在哈希表中查找），因此总体上比暴力解法的效率高得多。