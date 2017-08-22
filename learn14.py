def fact(n):
	if n is 1:
		return 1
	return n * fact(n - 1)


print(fact(5))
print(fact(10))
#使用递归函数需要注意防止栈溢出。在计算机中，函数调用是通过栈（stack）这种数据结构实现的，
#每当进入一个函数调用，栈就会加一层栈帧，每当函数返回，栈就会减一层栈帧。由于栈的大小不是无限的，
#所以，递归调用的次数过多，会导致栈溢出。
#解决递归调用栈溢出的方法是通过尾递归优化，事实上尾递归和循环的效果是一样的，所以，把循环看成是一种特殊的尾递归函数也是可以的。
#尾递归是指，在函数返回的时候，调用自身本身，并且，return语句不能包含表达式。
#这样，编译器或者解释器就可以把尾递归做优化，使递归本身无论调用多少次，都只占用一个栈帧，不会出现栈溢出的情况。

def fact1(n):
	return fact_iter(n, 1)

def fact_iter(num, product):
	if num is 1:
		return product
	return fact_iter(num-1, num*product)

print(fact1(5))
#遗憾的是，大多数编程语言没有针对尾递归做优化，
#Python解释器也没有做优化，所以，即使把上面的fact(n)函数改成尾递归方式，也会导致栈溢出。

def move(n, a, b, c):  #参数n表示3个柱子A、B、C中第1个柱子A的盘子数量，然后打印出把所有盘子从A借助B移动到C的方法
	if n is 1:
		print('%s-->%s'%(a, c))
		return
	return move(n-1, a, c, b), move(1, a, b, c), move(n-1, b, a, c)
#汉诺塔:在一根柱子上从下往上按照大小顺序摞着n片黄金圆盘。大梵天命令婆罗门把圆盘从下面开始按大小顺序重新摆放在另一根柱子上。
#并且规定，在小圆盘上不能放大圆盘，在三根柱子之间一次只能移动一个圆盘。
#思路：n个圆盘按要求从A柱移到C柱分为三步：1、先把n-1个圆盘移到B柱；2、再把最大的圆盘从A移到C；3、在把n-1个圆盘从B移到C。

move(3, 'A', 'B', 'C')