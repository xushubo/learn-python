#列表生成式即List Comprehensions，是Python内置的非常简单却强大的可以用来创建list的生成式。
L = list(range(10))  #生成0-9的列表  range(1, 10)生成1-9的列表
print(L)
M = [x * x for x in range(1, 11)]  #生成[1x1, 2x2, 3x3, ..., 10x10]
print(M)
N = [x * x for x in range(1, 11) if x % 2 is 0]  #for循环后面还可以加上if判断，这样我们就可以筛选出仅偶数的平方
print(N)
P = [m + n for m in 'ABC' for n in 'XYZ']  #使用两层循环，可以生成全排列
print(P)
Q = [a + b + c for a in 'AB' for b in 'CD' for c in 'EF'] #三层和三层以上的循环就很少用到了。
print(Q)

import os
R = [d for d in os.listdir('.')]  #运用列表生成式，可以写出非常简洁的代码。例如，列出当前目录下的所有文件和目录名，可以通过一行代码实现
print(R)

d = {'x': 'A', 'y': 'B', 'z': 'C'}  #for循环其实可以同时使用两个甚至多个变量，比如dict的items()可以同时迭代key和value
for k, v in d.items():
	print(k, '=', v)

S = [k + '=' + v for k, v in d.items()]
print(S)

T = ['Hello', 'World', 'IBM', 'Apple']  #把一个list中所有的字符串变成小写
U = [k.lower() for k in T]
print(U)

L1 = ['Hello', 'World', 18, 'Apple', None]  #使用内建的isinstance函数可以判断一个变量是不是字符串
L2 = [i.lower() for i in L1 if isinstance(i, str)]
print(L2)