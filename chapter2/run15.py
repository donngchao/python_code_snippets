# encoding: utf-8
'''
@author: developer
@software: python
@file: run15.py
@time: 2021/7/30 22:48
@desc:
'''

'''
描述
根据邮件的重量和用户是否选择加急计算邮费。计算规则：重量在1000克以内(包括1000克), 基本费8元。
超过1000克的部分，每500克加收超重费4元，不足500克部分按500克计算；如果用户选择加急，多收5元。

输入
输入一行，包含整数和一个字符，以一个空格分开，分别表示重量（单位为克）和是否加急。如果字符是y，说明选择加急；
如果字符是n，说明不加急。
输出
输出一行，包含一个整数，表示邮费。
样例输入
1200 y
样例输出
17
'''

input_str = input().split()
weight, fast = int(input_str[0]), input_str[1]
fee = 8

if weight <= 1000:
    fee += 0
elif weight > 1000:
    if weight - 1000 <= 500:
        fee += 4
    else:
        fee += ((weight - 1000) // 500 + 1) * 4

if fast == 'y':
    fee += 5
else:
    pass

print(fee)
