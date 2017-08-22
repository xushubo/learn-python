import itertools

natuals = itertools.count(1) #count()会创建一个无限的迭代器
for i in natuals:
	print(i)
	if i >= 10:
		break


cs = itertools.cycle('ABC') #cycle()会把传入的一个序列无限重复下去

n = 0
for i in cs:
	print(i)
	n = n + 1
	if n >= 10:
		break

ns = itertools.repeat('a', 5) #repeat()负责把一个元素无限重复下去，不过如果提供第二个参数就可以限定重复次数

for i in ns:
	print(i)

natuals1 = itertools.count(5)
#无限序列虽然可以无限迭代下去，但是通常我们会通过takewhile()等函数根据条件判断来截取出一个有限的序列
na = itertools.takewhile(lambda x: x <= 10, natuals1)
print(list(na))


for c in itertools.chain('ABC', 'XYZ'):  #chain()可以把一组迭代对象串联起来，形成一个更大的迭代器
	print(c)


for key, group in itertools.groupby('AAASbGGCCC'):  #groupby()把迭代器中相邻的重复元素挑出来放在一起
	print(key, list(group))

#实际上挑选规则是通过函数完成的，只要作用于函数的两个元素返回的值相等，
#这两个元素就被认为是在一组的，而函数返回值作为组的key。
#如果我们要忽略大小写分组，就可以让元素'A'和'a'都返回相同的key：
for key, group in itertools.groupby('aaaAAABbBbbbBB', lambda x: x.upper()):
	print(key, list(group))

