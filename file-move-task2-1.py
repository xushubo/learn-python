import os

def SearchStrFile(path, sstr):
	for x in os.listdir(path):
		if os.path.isfile(os.path.join(path, x)):
			if x.count(sstr):
				print('相对路径：', os.path.split(path)[1], x)
		else:
			SearchStrFile(os.path.join(path, x), sstr)




path = input('请输入要查找的文件夹路径:')
str1 = input('请输入要查找文件名包含的字符串：')
#expath = path.replace('/', '//')


SearchStrFile(path,str1)