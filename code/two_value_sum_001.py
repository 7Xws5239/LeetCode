from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        print("")
    test1 = ""
    def __init__(self) -> None:
        self.test1 = "001"
    def change_test1(self, test1):
        self.test1 = test1
class Solution2:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        print("")
    test2 = ""
    @classmethod
    def __init__(self) -> None:
        self.test2 = "002"
    @classmethod
    def change_test2(self, test2): #如果是静态方法就没有self参数了
        self.test2 = test2
    @staticmethod
    def static_method(cls):
        print("static_method")
    @staticmethod
    def static_method_with_self(self):
        print("static_method_with_self")
class NameInfo:
    _name = "_name is here." #这是一个命名规定，说明这是私有的from module import *的时候不会被导入
    __name = "__name is here." #这是会自动改名的
    def __name__(self) -> None:
        return "this is __name__ method."
    def print_name(self):
        print(self._name)
        print(self.__name)
        print(self._NameInfo__name)

NameInfo().print_name()

# value1 = NameInfo._name = "this is _name."
# value2 = NameInfo.__name = "this is __name."
# value3 = NameInfo().__name__()
# print(value1)
# print(value2)
# print(value3)

# 这种写法是错误的，因为这里面不是一个类方法或静态方法,也不是一个类属性
# print("test1: ", Solution.test1)
# Solution.change_test1(test1="test1")
# print("test1: ", Solution.test1)

# sln_instance = Solution()
# # Solution.__init__() #这个是不能这样用的
# print("test1: ", sln_instance.test1)
# sln_instance.change_test1(test1="test1")
# print("test1: ", sln_instance.test1)

# Solution2.__init__()
# print("test2: ", Solution2.test2)
# Solution2.change_test2(test2="test2")
# print("test2: ", Solution2.test2)

# Solution2.static_method(Solution2)
# Solution2.static_method_with_self("test")

'''
在您的代码中，您对 `Solution` 和 `Solution2` 类的处理方式有些混淆，尤其是在如何正确使用构造函数（`__init__`）和类方法上。我将逐个解释这些问题以及为什么 `Solution.__init__()` 的调用会出错，而 `Solution2.__init__()` 能够正常工作。

### 关于 `Solution` 类：

1. **`Solution.__init__()`**：`__init__` 是一个特殊方法，用作类的构造函数。当您创建类的实例时，这个方法会自动被调用。直接调用 `Solution.__init__()` 是不正确的做法，因为这是实例方法，需要一个 `Solution` 类的实例作为第一个参数。正确的做法是创建一个实例，让 Python 自动调用 `__init__` 方法：

    ```python
    sln_instance = Solution()
    # 这时，sln_instance.test1 已经被初始化为 "001"
    ```

### 关于 `Solution2` 类：

1. **类方法的错误使用**：您将 `__init__` 方法标记为了 `@classmethod`，这是不合适的。`__init__` 应该是一个普通的实例方法。将其标记为类方法会导致一些非预期的行为，尤其是在初始化实例时。

2. **类方法 `change_test2`**：虽然您将 `change_test2` 方法标记为 `@classmethod`，但通常类方法的第一个参数被命名为 `cls` 而不是 `self`，以区分于实例方法。类方法主要用于需要访问或修改类属性而不是实例属性的场景。

3. **为什么 `Solution2.__init__()` 可以工作**：由于您将 `__init__` 方法标记为 `@classmethod`，它变成了类方法而不是实例方法。因此，调用 `Solution2.__init__()` 实际上是在调用类方法而不是初始化一个实例。这是一种非标准和不推荐的用法。

### 修改后的代码：

为了让您的代码按预期工作，您应该这样写：

```python
from typing import List

class Solution:
    def __init__(self) -> None:
        self.test1 = "001"

    def change_test1(self, test1):
        self.test1 = test1

class Solution2:
    def __init__(self) -> None:
        self.test2 = "002"

    @classmethod
    def change_test2(cls, test2):
        cls.test2 = test2

# 正确使用 Solution 类
sln_instance = Solution()
print("test1: ", sln_instance.test1)
sln_instance.change_test1(test1="test1")
print("test1: ", sln_instance.test1)

# 正确使用 Solution2 类
sln2_instance = Solution2()
print("test2: ", sln2_instance.test2)
Solution2.change_test2(test2="test2")
print("test2: ", Solution2.test2)
```

在这个修改后的代码中：

- `Solution` 类的实例方法按照预期工作。
- `Solution2` 类的类方法用于修改类属性。这里我假设 `test2` 应该是一个类属性。如果它是一个实例属性，那么 `change_test2` 不应该是类方法。
'''