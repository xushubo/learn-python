#如果列表元素可以按照某种算法推算出来，那我们是否可以在循环的过程中不断推算出后续的元素呢？
#这样就不必创建完整的list，从而节省大量的空间。在Python中，这种一边循环一边计算的机制，称为生成器：generator

#要创建一个generator，有很多种方法。第一种方法很简单，只要把一个列表生成式的[]改成()，就创建了一个generator：
L = [x * x for x in range(10)]
print(L)
g = (x * x for x in range(10))
print(g)
print(next(g))  #如果要一个一个打印出来，可以通过next()函数获得generator的下一个返回值：
print(next(g))
print(next(g))

h = (x * x for x in range(10))
for n in h:  #上面这种不断调用next(g)实在是太繁琐了，正确的方法是使用for循环，因为generator也是可迭代对象
	print(n)

#如果推算的算法比较复杂，用类似列表生成式的for循环无法实现的时候，还可以用函数来实现。
#比如，著名的斐波拉契数列（Fibonacci），除第一个和第二个数外，任意一个数都可由前两个数相加得到：
#1, 1, 2, 3, 5, 8, 13, 21, 34, ...
#斐波拉契数列用列表生成式写不出来，但是，用函数把它打印出来却很容易：
def fib(max):
	n, a, b = 0, 0, 1
	while n < max:
		print(b)
		a, b = b, a+b  #相当于：t = (b, a + b)  t是一个tuple,a = t[0],b = t[1].但不必显式写出临时变量t就可以赋值。
		n = n + 1
	return 'done'
print(fib(6))

#要把fib函数变成generator，只需要把print(b)改为yield b就可以了：

def fibs(max):
	n, a, b = 0, 0, 1
	while n < max:
		yield b
		a, b = b, a + b
		n = n + 1
	return 'done'
print(fibs(6))  #如果一个函数定义中包含yield关键字，那么这个函数就不再是一个普通函数，而是一个generator
print(next(fibs(5)))

#generator和函数的执行流程不一样。函数是顺序执行，遇到return语句或者最后一行函数语句就返回。
#而变成generator的函数，在每次调用next()的时候执行，遇到yield语句返回，再次执行时从上次返回的yield语句处继续执行。

#把函数改成generator后，我们基本上从来不会用next()来获取下一个返回值，而是直接使用for循环来迭代：
j = fibs(5)
for n in j:
	print(n)

#但是用for循环调用generator时，发现拿不到generator的return语句的返回值。
#如果想要拿到返回值，必须捕获StopIteration错误，返回值包含在StopIteration的value中：
k = fibs(6)
while True:
	try:
		x = next(k)
		print('k:', x)
	except StopIteration as e:
		print('Generator return value:', e.value)
		break

def triangles():
	n = 0
	while True:
		m = 0
		L[n] = list(range(n+1))
		while m <= n:
			if m is 0:
				L[n][m] = 1
			elif m < n:
				L[n][m] = L[n-1][m-1]+L[n-1][m]
			elif m == n:
				L[n][m] = 1
				break
			m = m + 1
		yield L[n]
		n = n + 1
	return

def triangle():  #上述函数的精简版
	L = [1]
	while True:
		yield L
		L.append(0)
		L = [L[i-1] + L[i] for i in range(len(L))]

n = 0
for t in triangles():
	print(t)
	n = n + 1
	if n == 10:
		break

m = 0
for t in triangle():
	print(t)
	m = m + 1
	if m == 10:
		break