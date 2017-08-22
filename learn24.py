#Python内置的sorted()函数就可以对list进行排序：
print(sorted([36, 5, -12, 9, -21]))

#sorted()函数也是一个高阶函数，它还可以接收一个key函数来实现自定义的排序，例如按绝对值大小排序：
L= sorted([36, 5, -12, 9, -21], key=abs)
print(L)

#默认情况下，对字符串排序，是按照ASCII的大小比较的，由于'Z' < 'a'，结果，大写字母Z会排在小写字母a的前面。
M = sorted(['bob', 'about', 'Zoo', 'Credit'])
print(M)

#给sorted传入key函数，即可实现忽略大小写的排序：
N = sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower)
print(N)

#要进行反向排序，不必改动key函数，可以传入第三个参数reverse=True：
P = sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower, reverse=True)
print(P)

#假设我们用一组tuple表示学生名字和成绩,请用sorted()对上述列表分别按名字排序：
Q = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
print(sorted(Q, key=tuple))

def by_name(t):
	return t[0]
print(sorted(Q, key=by_name))

#按分数排序：
def by_score(t):
	return t[1]
print(sorted(Q, key=by_score))

#sorted函数也可以进行多级排序，例如要根据第二个域和第三个域进行排序,即先根据第二个域排序，再根据第三个域排序。
from operator import itemgetter
students = [('Bob', 'B', 75), ('Adam', 'A', 92), ('Bart', 'C', 66), ('Lisa', 'A', 88)]
print(sorted(students, key=itemgetter(1, 2)))
print(sorted(students, key=lambda students: students[2]))

'''
operator.itemgetter函数
operator模块提供的itemgetter函数用于获取对象的哪些维的数据，参数为一些序号（即需要获取的数据在对象中的序号），下面看例子。

a = [1,2,3] 
>>> b=operator.itemgetter(1)      //定义函数b，获取对象的第1个域的值
>>> b(a) 
2 
>>> b=operator.itemgetter(1,0)  //定义函数b，获取对象的第1个域和第0个的值
>>> b(a) 
(2, 1)

要注意，operator.itemgetter函数获取的不是值，而是定义了一个函数，通过该函数作用到对象上才能获取值。
'''