classmates=['Michael','Bob','Tracy']
print(classmates)
print(len(classmates))#如果要取最后一个元素，除了计算索引位置外，还可以用-1做索引，直接获取最后一个元素,以此类推，可以获取倒数第2个、倒数第3个
print(classmates[0],classmates[1],classmates[-1],classmates[-2])
classmates.append('Adm')#list是一个可变的有序表，所以，可以往list中追加元素到末尾
print(classmates)
classmates.insert(1,'Jack')#也可以把元素插入到指定的位置，比如索引号为1的位置
print(classmates)
classmates.pop()#除list末尾的元素，用pop()方法
print(classmates)
classmates.pop(1)#要删除指定位置的元素，用pop(i)方法，其中i是索引位置
print(classmates)
classmates[1]='Sarah'#要把某个元素替换成别的元素，可以直接赋值给对应的索引位置
print(classmates)
L=['Apple',123,True]#list里面的元素的数据类型也可以不同
print(L)
s=['python','java',['asp','php'],'scheme']#list元素也可以是另一个list
print(len(s))#要注意s只有4个元素，其中s[2]又是一个list
p=['asp','php']
q=['python','java',p,'scheme']#要拿到'php'可以写p[1]或者q[2][1]，因此s可以看成是一个二维数组
print(q[2][1])
U=[]#如果一个list中一个元素也没有，就是一个空的list，它的长度为0
print(len(U))