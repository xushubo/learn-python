t=[5,3,6,4,7,345,35]
print(max(t))
m=max#函数名其实就是指向一个函数对象的引用，完全可以把函数名赋给一个变量，相当于给这个函数起了一个“别名”
print(m(t))
print(abs(-20),abs(100),abs(8.8),abs(-9.1))
print(hex(368))#利用Python内置的hex()函数把一个整数转换成十六进制表示的字符串
print(bool(3),bool(0),bool(),bool(-2.1))#bool函数只有传入的参数是0或者空返回值是False，其余均为True
print(int('123'),float('12.34'),str(123))#Python内置的常用函数还包括数据类型转换函数，比如int()函数可以把其他数据类型转换为整数
n1 = 255
n2 = 1000
n3 = 25.25
print(hex(n1),hex(n2))#hex()函数返回值是str类型
print(float.hex(n3))#浮点数需用float.hex()来转换成16进制