def my_abs(x):             #函数体内部的语句在执行时，一旦执行到return时，函数就执行完毕，并将结果返回。
	if x >= 0:             #如果没有return语句，函数执行完毕后也会返回结果，只是结果为None。return None可以简写为return
		return x           #如果你已经把my_abs()的函数定义保存为abstest.py文件了，那么，
	else:                  #可以在该文件的当前目录下启动Python解释器，用from abstest import my_abs来导入my_abs()函数，
		return -x          #注意abstest是文件名（不含.py扩展名）
print(my_abs(12),my_abs(-1.1))

def nop():				   #如果想定义一个什么事也不做的空函数，可以用pass语句
	pass

#pass语句什么都不做，那有什么用？实际上pass可以用来作为占位符，比如现在还没想好怎么写函数的代码，
#就可以先放一个pass，让代码能运行起来。
#pass还可以用在其他语句里，比如：
#if age >= 18:
#    pass
#缺少了pass，代码运行就会有语法错误。

#当传入了不恰当的参数时，内置函数abs会检查出参数错误，而我们定义的my_abs没有参数检查，
#会导致if语句出错，出错信息和abs不一样。所以，这个函数定义不够完善。
#让我们修改一下my_abs的定义，对参数类型做检查，只允许整数和浮点数类型的参数。数据类型检查可以用内置函数isinstance()实现
#添加了参数检查后，如果传入错误的参数类型，函数就可以抛出一个错误
def My_abs(x):
	if not isinstance(x,(int,float)):
		raise TypeError('bad operand type')
	if x >= 0:
		return x
	else:
		return -x

import math               #导入math包，并允许后续代码引用math包里的sin、cos等函数
def move(x,y,step,angle=0):
	nx = x + step * math.cos(angle)
	ny = y + step * math.sin(angle)
	return nx,ny
x,y = move(100,100,60,math.pi / 6)#返回值是一个tuple！但是，在语法上，返回一个tuple可以省略括号
print(x,y)                        #而多个变量可以同时接收一个tuple，按位置赋给对应的值，
r = move(100,100,60,math.pi / 6)  #所以，Python的函数返回多值其实就是返回一个tuple，但写起来更方便。
print(r)

def quadratic(a,b,c):
	if not isinstance(a,(int,float)):
		raise TypeError('first parameter bad operand type')
	if not isinstance(b,(int,float)):
		raise TypeError('second parameter bad operand type')
	if not isinstance(c,(int,float)):
		raise TypeError('third parameter bad operand type')
	if a == 0:
		print('当前输入的参数为一元一次方程，仅有一个解为x=',-c/b)
		return -c/b
	if (b**2-4*a*c)<0:
		print ('一元二次方程无实数根')
		return
	else:
		print('一元二次方程两个解为：x1=%.2f,x2=%.2f'%((-b+math.sqrt(b**2-4*a*c))/(2*a),(-b-math.sqrt(b**2-4*a*c))/(2*a)))

quadratic(0,2,1)
quadratic(1,5,1)
quadratic(4,2,2)
quadratic(2,3,1)
quadratic(1,3,-4)
quadratic('abc',2,1)