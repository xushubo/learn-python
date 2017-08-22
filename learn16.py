#如果给定一个list或tuple，我们可以通过for循环来遍历这个list或tuple，这种遍历我们称为迭代（Iteration）。
d = {'a': 1, 'b': 2, 'c': 3}
for key in d:  #默认情况下，dict迭代的是key
	print(key)
	print(d[key])

for value in d.values():  #如果要迭代value，可以用for value in d.values()
	print(value)

for k, v in d.items():  #如果要同时迭代key和value，可以用for k, v in d.items()
	print(k,v)

for ch in 'abcdsgsd':  #由于字符串也是可迭代对象，因此，也可以作用于for循环
	print(ch)

#所以，当我们使用for循环时，只要作用于一个可迭代对象，for循环就可以正常运行，而我们不太关心该对象究竟是list还是其他数据类型。
#如何判断一个对象是可迭代对象呢？方法是通过collections模块的Iterable类型判断：
from collections import Iterable

isinstance('abc', Iterable)  #str是否可迭代,如果可以迭代，会返回true，反之，返回false
isinstance([1,2,3], Iterable)  #list是否可迭代
isinstance(123, Iterable)  #整数是否可迭代

#Python内置的enumerate函数可以把一个list变成索引-元素对，这样就可以在for循环中同时迭代索引和元素本身：
for i, value in enumerate(['A', 'B', 'C']):
	print(i,value)

for x, y in [(1,2), (2,3), (3,4)]:  #for循环里，同时引用了两个变量，在Python里是很常见的
	print(x,y)

#任何可迭代对象都可以作用于for循环，包括我们自定义的数据类型，只要符合迭代条件，就可以使用for循环。