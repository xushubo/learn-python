s=input('birth:')
birth=int(s)            #input()返回的数据类型是str，str不能直接和整数比较，必须先把str转换成整数。
if birth<2000:
	print('00前')
else:
	print('00后')

height = 1.75
weight = 80.5
BMI = weight/(height*height)
if BMI>32:
	print('严重肥胖')
elif BMI>=28:
	print('肥胖')
elif BMI>=25:
	print('过重')
elif BMI>=18.5:
	print('正常')
else:
	print('过轻')