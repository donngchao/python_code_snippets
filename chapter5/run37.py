# encoding: utf-8
'''
@author: developer
@software: python
@file: run37.py
@time: 2021/8/22 20:11
@desc:
'''


'''
描述
输入一个字符串，输出该字符串是否回文。回文是指顺读和倒读都一样的字符串。

输入
输入为一行字符串（字符串中没有空白字符，字符串长度不超过100）。
输出
如果字符串是回文，输出yes；否则，输出no。
样例输入
abcdedcba
样例输出
yes
'''

test_str = input()
test_str_reverse = test_str[::-1]

if test_str == test_str_reverse:
    print("yes")
else:
    print("no")


