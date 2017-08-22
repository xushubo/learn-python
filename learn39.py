class Student(object):
	__slots__ = ('name', 'age', 'score', 'set_age') #Python允许在定义class的时候，定义一个特殊的__slots__变量，来限制该class实例能添加的属性,只能限时该类的实例，不能限制类本身
	pass

s = Student()
s.name = 'Michael'
print(s.name)

def set_age(self, age):
	self.age = age

from types import MethodType

s.set_age = MethodType(set_age, s)
s.set_age(25)
print(s.age)

def set_score(self, score):
	self.score = score

Student.set_score = set_score

s.set_score(98)
print(s.score)

s2 = Student()

s2.set_score(78)
print(s2.score)

class GraduateStudent(Student):
	__slots__ = ('sex', 'date') #使用__slots__要注意，__slots__定义的属性仅对当前类实例起作用，对继承的子类是不起作用的,除非在子类中也定义__slots__，这样，子类实例允许定义的属性就是自身的__slots__加上父类的__slots__。

g = GraduateStudent()
g.sex = 'man'
print(g.sex)
g.age = 18
print(g.age)

def set_graduation_date(self, date):
	self.date = date

GraduateStudent.set_graduation_date = set_graduation_date
g.set_graduation_date('2005-09-01')
print(g.date)