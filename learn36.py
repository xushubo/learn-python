class Student(object):
	def __init__(self, name, score):
		self.name = name
		self.score = score

	def print_score(self):
		print('%s: %s' % (self.name, self.score))

	def get_grade(self):
		if self.score >= 90:
			return 'A'
		elif self.score >= 60:
			return 'B'
		else:
			return 'C'

bart = Student('Bart Simpson', 89)
print(bart)
print(Student)
bart.name = 'Bart Simpson1'
print(bart.name)
print(bart.score)
bart.print_score()
print(bart.get_grade())
bart.age = 18 #Python允许对实例变量绑定任何数据，也就是说，对于两个实例变量，虽然它们都是同一个类的不同实例，但拥有的变量名称都可能不同
print(bart.age)



class Rectangle(object):
	def __init__(self, length, width):
		self.__length = length
		self.__width = width

	def print_data(self):
		if self.__length <= 0 or self.__width <= 0:
			print('this Rectangle is non-existent')
		else:
			print('Rectangle\'s legth: %s,width: %s' % (self.__length, self.__width))

	def get_length(self):
		return self.__length

	def get_width(self):
		return self.__width

	def set_length(self, length):
		self.__length = length

	def set_width(self, width):
		self.__width = width

	def area(self):
		return self.__length * self.__width
	
	def type(self):
		if self.__length <= 0 or self.__width <= 0:
			return 'this Rectangle is non-existent'
		elif self.__length == self.__width:
			return 'Square'
		else:
			return 'Rectangle'

A = Rectangle(6, 4)
B = Rectangle(5, 5)
C = Rectangle(0, 5)
print(A.type())
print(B.type())
print(C.type())
A.print_data()
B.print_data()
C.print_data()

A_a = A.get_length()
A_b = A.get_width()
print(A_a, A_b)

A.set_length(8)
A.set_width(6)
A.print_data()
A._Rectangle__length = 7 #不能直接访问__name是因为Python解释器对外把__name变量改成了_Student__name，所以，仍然可以通过_Student__name来访问__name变量
A.print_data()