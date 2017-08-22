a='ABC' #1、在内存中创建了一个'ABC'的字符串；2、在内存中创建了一个名为a的变量，并把它指向'ABC'。
b=a     #也可以把一个变量a赋值给另一个变量b，这个操作实际上是把变量b指向变量a所指向的数据。
a='XYZ'
print(a,b)
print(10/3)
print(9/3)#除法计算结果是浮点数，即使是两个整数恰好整除，结果也是浮点数。
print(10//3)#还有一种除法是//，称为地板除，两个整数的除法仍然是整数。
print(10.0//3)
print(10%3)#取余数
n = 123
f = 456.789
s1 = 'Hello, world'
s2 = 'Hello, \'Adam\''
s3 = r'Hello, "Bart"'
s4 = r'''Hello,
Lisa!'''
print (n)
print (f)
print (s1)
print (s2)
print (s3)
print (s4)
