def power(x, n=2):  #必选参数在前，默认参数在后
	if x is not 0:
		return x**n
	else:
		return 0

print(power(2, 4))
print(power(2, -2))
print(power(2))
print(power(0, -4))

def enroll(name, gender, age=6, city='beijing'):  #只有与默认参数不符的学生才需要提供额外的信息
	print('name:', name, ' gender:', gender, ' age:', age, ' city:', city,sep='')

enroll('Bob', 'M')
enroll('Bob', 'M', 7)
enroll('Bob', 'M', city='tianjin')  #当不按顺序提供部分默认参数时，需要把参数名写上
enroll('Bob', 'M', city='guangzhou', age=8)
enroll('Bob', 'M', 7, 'shanghai')


def add_end(L=[]):
	L.append('END')
	return L

print(add_end([1,2,3]))  #当你正常调用时，结果似乎不错
print(add_end(['x', 'y', 'z']))
print(add_end())  #当你使用默认参数调用时，一开始结果也是对的
print(add_end())  #再次调用add_end()时，结果就不对了

#Python函数在定义的时候，默认参数L的值就被计算出来了，即[]，
#因为默认参数L也是一个变量，它指向对象[]，每次调用该函数，
#如果改变了L的内容，则下次调用时，默认参数的内容就变了，不再是函数定义时的[]了。
#所以，定义默认参数要牢记一点：默认参数必须指向不变对象！
#要修改上面的例子，我们可以用None这个不变对象来实现：

def add_ends(L=None):
	if L is None:
		L=[]
	L.append('END')
	return L

print(add_ends())  #现在，无论调用多少次，都不会有问题
print(add_ends())

#为什么要设计str、None这样的不变对象呢？因为不变对象一旦创建，
#对象内部的数据就不能修改，这样就减少了由于修改数据导致的错误。
#此外，由于对象不变，多任务环境下同时读取对象不需要加锁，
#同时读一点问题都没有。我们在编写程序时，如果可以设计一个不变对象，那就尽量设计成不变对象。

#定义可变参数和定义一个list或tuple参数相比，仅仅在参数前面加了一个*号。
#在函数内部，参数numbers接收到的是一个tuple，因此，函数代码完全不变。
#但是，调用该函数时，可以传入任意个参数，包括0个参数：

def calc(*numbers): #可变参数
	sum = 0
	for n in numbers:
		sum = sum + n * n
	return sum
nums = [1, 2, 3]
print(calc(nums[0], nums[1], nums[2]))  #这种写法当然是可行的，问题是太繁琐
print(calc(*nums))  #Python允许在list或tuple前面加一个*号，把list或tuple的元素变成可变参数传进去

#*nums表示把nums这个list的所有元素作为可变参数传进去。这种写法相当有用，而且很常见。

#关键字参数允许你传入0个或任意个含参数名的参数，这些关键字参数在函数内部自动组装为一个dict。

def person(name, age, **kw):
	print('name:', name, 'age:', 'other:', kw)

person('Michael', 30)  #在调用该函数时，可以只传入必选参数
person('Bob', 25, city='beijing')  #也可以传入任意个数的关键字参数
person('Adam', 35, gender='M', job='Engineer')
extra = {'city': 'beijing', 'job': 'Engineer'}
person('Jack', 24, city=extra['city'], job=extra['job'])
person('Jack', 24, **extra)
#**extra表示把extra这个dict的所有key-value用关键字参数传入到函数的**kw参数,
#kw将获得一个dict，注意kw获得的dict是extra的一份拷贝，对kw的改动不会影响到函数外的extra。

#如果要限制关键字参数的名字，就可以用命名关键字参数，例如，只接收city和job作为关键字参数。
#和关键字参数**kw不同，命名关键字参数需要一个特殊分隔符*，*后面的参数被视为命名关键字参数。
def persons(name, age, *, city, job):
	print(name, age, city, job)

persons('Jack', 24, city='beijing', job='Engineer')
persons('Jack', 24, job='Engineer', city='beijing')  #命名关键字参数顺序可以调换，不会改变函数结果

#如果函数定义中已经有了一个可变参数，后面跟着的命名关键字参数就不再需要一个特殊分隔符*了：
#def person(name, age, *args, city, job):
#    print(name, age, args, city, job)
#命名关键字参数必须传入参数名，这和位置参数不同。如果没有传入参数名，调用将报错
#person('Jack', 24, 'Beijing', 'Engineer')
#命名关键字参数可以有缺省值，从而简化调用 def person(name, age, *, city='Beijing', job)
#由于命名关键字参数city具有默认值，调用时，可不传入city参数

#在Python中定义函数，可以用必选参数、默认参数、可变参数、关键字参数和命名关键字参数，
#这5种参数都可以组合使用。
#但是请注意，参数定义的顺序必须是：必选参数、默认参数、可变参数、命名关键字参数和关键字参数。

def f1(a, b, c=0, *args, **kw):
	print('a=', a, 'b=', b, 'c=', c,'args=', args, 'kw=', kw)

def f2(a, b, c=0, *, d, **kw):
	print('a =', a, 'b =', b, 'c =', c, 'd =', d, 'kw =', kw)

f1(1,2)
f1(1,2,c=3)