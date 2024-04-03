# 重新组织文件夹和文件信息，结合第二部分文本的具体题目描述
folders_and_files_updated = [
    {
        "folder": "双指针two pointers",
        "files": [
            "141_Linked_List_Cycle.py",
            "344_Reverse_String.py",
            "881_Boats_to_Save_People.py"
        ]
    },
    {
        "folder": "二分查找 binary search",
        "files": [
            "704_Binary_Search.py",
            "35_Search_Insert_Position.py",
            "162_Find_Peak_Element.py",
            "74_Search_a_2D_Matrix.py"
        ]
    },
    {
        "folder": "滑动窗口 sliding window",
        "files": [
            "209_Minimum_Size_Subarray_Sum.py",
            "1456_Maximum_Number_of_Vowels_in_a_Substring_of_Given_Length.py"
        ]
    },
    {
        "folder": "递归 recursion",
        "files": [
            "509_Fibonacci_Number.py",
            "206_Reverse_Linked_List.py",
            "344_Reverse_String.py",  # 注意：与双指针算法重复
            "687_Longest_Univalue_Path.py"
        ]
    },
    {
        "folder": "分治 divide&conquer",
        "files": [
            "169_Majority_Element.py",
            "53_Maximum_Subarray.py"
        ]
    },
    {
        "folder": "回溯 backtracking",
        "files": [
            "22_Generate_Parentheses.py",
            "78_Subsets.py",
            "77_Combinations.py",
            "46_Permutations.py"
        ]
    },
    {
        "folder": "深度优先搜索DFS",
        "files": [
            "938_Range_Sum_of_BST.py",
            "78_Subsets.py",  # 注意：与回溯算法重复
            "200_Number_of_Islands.py"
        ]
    },
    {
        "folder": "宽度优先搜索BFS",
        "files": [
            "102_Binary_Tree_Level_Order_Traversal.py",
            "107_Binary_Tree_Level_Order_Traversal_II.py",
            "200_Number_of_Islands.py"  # 注意：与深度优先搜索重复
        ]
    },
    {
        "folder": "并查集 union find",
        "files": [
            "200_Number_of_Islands.py",  # 注意：与深度优先搜索和宽度优先搜索重复
            "547_Number_of_Provinces.py",
            "721_Accounts_Merge.py"
        ]
    },
    {
        "folder": "贪心 greedy",
        "files": [
            "322_Coin_Change.py",
            "1217_Minimum_Cost_to_Move_Chips_to_The_Same_Position.py",
            "55_Jump_Game.py"
        ]
    },
    {
        "folder": "记忆化搜索",
        "files": [
            "509_Fibonacci_Number.py",  # 注意：与递归算法重复
            "322_Coin_Change.py"  # 注意：与贪心算法重复
        ]
    },
    {
        "folder": "动态规划 dynamic programming",
        "files": [
            "509_Fibonacci_Number.py",  # 注意：与递归算法和记忆化搜索重复
            "62_Unique_Paths.py",
            "121_Best_Time_to_Buy_and_Sell_Stock.py",
            "70_Climbing_Stairs.py",
            "279_Perfect_Squares.py",
            "221_Maximal_Square.py"
        ]
    },
    {
        "folder": "拓扑排序 topologic sort",
        "files": [
            "207_Course_Schedule.py",
            "210_Course_Schedule_II.py"
        ]
    },
    {
        "folder": "前缀树 trie",
        "files": [
            "208_Implement_Trie.py",
            "720_Longest_Word_in_Dictionary.py",
            "692_Top_K_Frequent_Words.py"
        ]
    },
]

import os
current_dir=os.getcwd()
# 使用更新后的文件夹和文件信息创建文件夹和文件
for item in folders_and_files_updated:
    folder_path = os.path.join(current_dir, item["folder"])
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
    for file_name in item["files"]:
        file_path = os.path.join(folder_path, file_name)
        if not os.path.exists(file_path):
            with open(file_path, "w") as f:
                pass 
