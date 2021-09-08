# encoding: utf-8
'''
@author: developer
@software: python
@file: run30.py
@time: 2021/8/8 8:02
@desc:
'''

'''
描述
给定两个正整数，求它们的最大公约数。

输入
输入一行，包含两个正整数(<1,000,000,000)。
输出
输出一个正整数，即这两个正整数的最大公约数。
样例输入
6 9
样例输出
3
提示
求最大公约数可以使用辗转相除法：
假设a > b > 0，那么a和b的最大公约数等于b和a%b的最大公约数，然后把b和a%b作为新一轮的输入。
由于这个过程会一直递减，直到a%b等于0的时候，b的值就是所要求的最大公约数。
比如：
9和6的最大公约数等于6和9%6=3的最大公约数。
由于6%3==0，所以最大公约数为3。

'''
input_val = input().split()
num1, num2 = int(input_val[0]), int(input_val[1])


def get_gcd(val1, val2):
    max_val = max(val1, val2)
    min_val = min(val1, val2)
    r = max_val % min_val
    while r != 0:
        get_gcd(min_val, r)
    print(min_val)
    exit()


get_gcd(num1, num2)
