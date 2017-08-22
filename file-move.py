import os
print(os.name)
print(os.environ)
print(os.environ.get('COMMONPROGRAMFILES(X86)'))
print(os.environ['COMSPEC'])


print(os.path.abspath('.')) # 查看当前目录的绝对路径
m = os.path.join('C:\\Users\\DestoryBlue\\AppData\\Roaming\\Sublime Text 3\\Packages\\User\\python', 'destroy')
print(m)  #把新目录的完整路径表示出来
os.mkdir('C:\\Users\\DestoryBlue\\AppData\\Roaming\\Sublime Text 3\\Packages\\User\\python\\destroy') #创建
os.rmdir('C:\\Users\\DestoryBlue\\AppData\\Roaming\\Sublime Text 3\\Packages\\User\\python\\destroy') #删除

print(os.path.split('/Users/michael/testdir/file.txt')) #把一个路径拆分为两部分，后一部分总是最后级别的目录或文件名
print(os.path.splitext('/Users/michael/testdir/file.txt')) #可以直接让你得到文件扩展名

#os.rename('test.txt', 'test.py')
#os.remove('test.py')

print(os.listdir('C:\\Users\\DestoryBlue\\Desktop'))
print(os.path.isdir('HSS'))
for x in os.listdir('C:\\Users\\DestoryBlue\\Desktop'):
	full_dir_file = os.path.join('C:\\Users\\DestoryBlue\\Desktop', x)
	if os.path.isdir(full_dir_file):
		print(x)
'''
在上面的for/in循环中，x实际上只是一个文件名。测试发现，当我使用os.path.isdir(目录的绝对路径)的时候，
返回的才是true，也就是说，Python的isdir()并不像PHP的is_dir()那样，可以使用当前工作目录的相对路径，
那么这里怎么样去改进这个备份文件呢？幸好python提供了一个os.path.join()函数，
自动来把需要的路径加到一块，而不用担心手动把路径字符串连接起来时，产生多余的”/”的问题
'''

l = [n for n in os.listdir('C:\\Users\\DestoryBlue\\Desktop') if os.path.isdir(os.path.join('C:\\Users\\DestoryBlue\\Desktop', n))]
print(l)

t = [m for m in os.listdir('C:\\Users\\DestoryBlue\\Desktop') if os.path.isfile(os.path.join('C:\\Users\\DestoryBlue\\Desktop', m)) and os.path.splitext(m)[1]=='.xlsx']
print(t)