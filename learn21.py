#map()函数接收两个参数，一个是函数，一个是Iterable，map将传入的函数依次作用到序列的每个元素，
#并把结果作为新的Iterator返回。
def f(x):
	return x * x
r = map(f,[1, 2, 3, 4, 5, 6, 7, 8, 9])  #map()传入的第一个参数是f，即函数对象本身。
print(list(r))  #由于结果r是一个Iterator，Iterator是惰性序列，因此通过list()函数让它把整个序列都计算出来并返回一个list。
#map()作为高阶函数，事实上它把运算规则抽象了，
#因此，我们不但可以计算简单的f(x)=x2，还可以计算任意复杂的函数，
#比如，把这个list所有数字转为字符串：
print(list(map(str,[1, 2, 3, 4, 5, 6, 7, 8, 9])))

#reduce把一个函数作用在一个序列[x1, x2, x3, ...]上，
#这个函数必须接收两个参数，reduce把结果继续和序列的下一个元素做累积计算，其效果就是：
#reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)
#比方说对一个序列求和，就可以用reduce实现：
from functools import reduce
def add(x, y):
	return x + y
print(reduce(add,[1, 3, 5, 7]))
#当然求和运算可以直接用Python内建函数sum()，没必要动用reduce。
#但是如果要把序列[1, 3, 5, 7, 9]变换成整数13579，reduce就可以派上用场：
def fn(x, y):
	return x * 10 + y
print(reduce(fn, [1, 3, 5, 7, 9]))
#如果考虑到字符串str也是一个序列，对上面的例子稍加改动，
#配合map()，我们就可以写出把str转换为int的函数：
def str2int(s):
	def fn(x, y):
		return x * 10 + y
	def char2num(s):
		return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]
	return reduce(fn, map(char2num, s))
print(str2int('1234'))

#还可以用lambda函数进一步简化成：
def char2num(s):
	return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]
def strs2int(s):
	return reduce(lambda x, y: x * 10 + y, map(char2num, s))
#lambda函数也叫匿名函数，即，函数没有具体的名称,而用def创建的方法是有名称的。
#lambda语句中，冒号前是参数，可以有多个，用逗号隔开，冒号右边是返回值。
print(strs2int('3456'))

def normalize(name):
	n = 0
	name1 = list(name)
	for i in name1:
		if n is 0:
			name1[n] = i.upper()
		else:
			name1[n] = i.lower()
		n = n + 1
	return ''.join(name1)

#	return name.capitalize() 

#和其他语言一样，Python为string对象提供了转换大小写的方法：upper() 和 lower()。
#还不止这些，Python还为我们提供了首字母大写，其余小写的capitalize()方法，以及所有单词首字母大写，其余小写的title()方法。

print(list(map(normalize, ['adam', 'LISA', 'barT'])))


def prod(L):
	def fm(x, y):
		return x * y
	return reduce(fm, L)  #return reduce(lambda x, y: x * y, L)
print('1 * 3 * 4 * 5 =', prod([1, 3, 4 ,5]))

def str2float(s):
	n = 0
	for i in s:
		if s[n] == '.':
			break
		n = n + 1
	news = s[:n] + s[n+1:]
	def fn(x, y):
		return x * 10 + y
	def char2num(s1):
		return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s1]
	return reduce(fn, map(char2num, news)) / 10 ** (len(news)-n)
print ('str2float(\'123.456\')=', str2float('123.456'))

def str2float1(s):
    n1,n2=s.split('.')  #s.split()是分割字符串函数，以小数点分割成两部分
    print(reduce(lambda x,y:x*10+y,map(lambda x:int(x),n1))+reduce(lambda x,y:(x*10+y),map(lambda x:int(x),n2))/10**len(n2))
str2float1('123.456')