# encoding: utf-8
'''
@author: developer
@software: python
@file: run41.py
@time: 2021/8/29 8:54
@desc:
'''

'''
描述
给出班里某门课程的成绩单，请你按成绩从高到低对成绩单排序输出，如果有相同分数则名字字典序小的在前。 

输入
第一行为n (0 < n < 20)，表示班里的学生数目；
接下来的n行，每行为每个学生的名字和他的成绩, 中间用单个空格隔开。名字只包含字母且长度不超过20，成绩为一个不大于100的非负整数。
输出
把成绩单按分数从高到低的顺序进行排序并输出，每行包含名字和分数两项，之间有一个空格。
样例输入
4
Kitty 80
Hanmeimei 90
Joey 92
Tim 28
样例输出
Joey 92
Hanmeimei 90 
Kitty 80
Tim 28
'''

num_of_students = int(input())
score_list = []

for i in range(num_of_students):
    input_info = input().split()
    score_list.append((input_info[0], int(input_info[1])))

score_list.sort(key=lambda x: (-x[1], x[0]))

for j in range(num_of_students):
    print(score_list[j][0]+" "+str(score_list[j][1]))
