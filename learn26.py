#当我们在传入函数时，有些时候，不需要显式地定义函数，直接传入匿名函数更方便。
#关键字lambda表示匿名函数，冒号前面的x表示函数参数。
#匿名函数有个限制，就是只能有一个表达式，不用写return，返回值就是该表达式的结果。
#用匿名函数有个好处，因为函数没有名字，不必担心函数名冲突。
#此外，匿名函数也是一个函数对象，也可以把匿名函数赋值给一个变量，再利用变量来调用该函数：
f = lambda x: x * x
print(f(5))

#同样，也可以把匿名函数作为返回值返回，比如：
def build(x, y):
	return lambda: x * x + y * y



def cacl():
	L = []
	for i in range(4, 6):
		def d():
			return i * i + 2
		L.append(d)
	return L

c1, c2 = cacl()
print(c1(), c2())

def cacls():
	def c(j):
		def g():
			return j * j + 2
		return g
	L = []
	for i in range(4, 6):
		L.append(c(i))
	return L
c3, c4 = cacls()
print(c3(), c4())