#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from functools import reduce

CHAR_TO_INT = {
    '0': 0,
    '1': 1,
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9
}

def str2int(s):
    ints = map(lambda ch: CHAR_TO_INT[ch], s)
    return reduce(lambda x, y: x * 10 + y, ints)

print(str2int('0'))
print(str2int('12300'))
print(str2int('0012345'))

CHAR_TO_FLOAT = {
    '0': 0,
    '1': 1,
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    '.': -1
}

def str2float(s):
    nums = map(lambda ch: CHAR_TO_FLOAT[ch], s)
    point = 0
    def to_float(f, n):
        nonlocal point
        if n == -1:
            point = 1
            return f
        if point == 0:
            return f * 10 + n
        else:
            point = point * 10
            return f + n / point
    return reduce(to_float, nums, 0.0)  
#当调用reduce方法的时候给出了第三个参数，那么第一次调用appFun的时候reduce的第三个参数值就作为appFun的第一个参数，
#而可迭代对象的元素依次作为appFun的第二个参数

print(str2float('0'))
print(str2float('123.456'))
print(str2float('123.45600'))
print(str2float('0.1234'))
print(str2float('.1234'))
print(str2float('120.0034'))
print(str2float('.1234111111'))

#有一个序列集合，例如[1,1,2,3,2,3,3,5,6,7,7,6,5,5,5],统计这个集合所有键的重复个数，
#例如1出现了两次，2出现了两次等。大致的思路就是用字典存储，元素就是字典的key,出现的次数就是字典的value。方法依然很多

lst = [1, 1, 2, 3, 2, 3, 3, 5, 6, 7, 7, 6, 5, 5, 5]

#第一种：for循环判断
def statistics_one(lst):
    dic = {}
    for k in lst:
        if k not in dic:
            dic[k] = 1
        else:
            dic[k] +=1
    return dic

print(statistics_one(lst))

#第二种：比较取巧的，先把列表用set方式去重，然后用列表的count方法
def statistics_two(lst):
    m = set(lst)
    dic = {}
    for k in m:
        dic[k] = lst.count(k)
    return dic

print(statistics_two(lst))

#第三种：用reduce方式
def statistics_three(dic, k):
    if not k in dic:
        dic[k] = 1
    else:
        dic[k] +=1
    return dic
print(reduce(statistics_three, lst, {}))