# encoding: utf-8
'''
@author: developer
@software: python
@file: run38.py
@time: 2021/8/22 20:37
@desc:
'''
'''
描述
有三个字符串S,S1,S2，其中，S长度不超过300，S1和S2的长度不超过10。
想检测S1和S2是否同时在S中出现，且S1位于S2的左边，并在S中互不交叉
（即，S1的右边界点在S2的左边界点的左侧）。
计算满足上述条件的最大跨距
（即，最大间隔距离：最右边的S2的起始点与最左边的S1的终止点之间的字符数目）。
如果没有满足条件的S1，S2存在，则输出-1。

例如，S = "abcd123ab888efghij45ef67kl", S1="ab", S2="ef"，其中，S1在S中出现了2次，S2也在S中出现了2次，
最大跨距为：18。

输入
三个串：S, S1, S2，其间以逗号间隔（注意，S, S1, S2中均不含逗号和空格）；
输出
S1和S2在S最大跨距；若在S中没有满足条件的S1和S2，则输出-1。
样例输入
abcd123ab888efghij45ef67kl,ab,ef
样例输出
18
'''

test_str = input().split(",")
left_index = test_str[0].find(test_str[1])
right_index = test_str[0].rfind(test_str[2])


if test_str[0].count(test_str[1]) != 0 and test_str[0].count(test_str[2]) != 0 and left_index+len(test_str[1]) <= right_index:
    print(right_index - left_index - len(test_str[1]))
else:
    print("-1")





