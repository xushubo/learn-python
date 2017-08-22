class Student(object):
#	__slots__ = ('_score')

	def get_score(self):
		return self._score

	def set_score(self, value):
		if not isinstance(value, int):
			raise ValueError('score must be an integer!')
		if value < 0 or value > 100:
			raise ValueError('score must between 0~100!')
		else:
			self._score = value

s = Student()
s.set_score(60)
print(s.get_score())
#s.set_score(991)


class Student1(object):
#	__slots__ = ('_score')

	@property
	def score(self):
		return self._score

	@score.setter
	def score(self, value):
		if not isinstance(value, int):
			raise ValueError('score must be an integer!')
		if value < 0 or value > 100:
			raise ValueError('score must between 0~100!')
		else:
			self._score = value

s1 = Student1()
s1.score = 60 # OK，实际转化为s.set_score(60)
print(s1.score) # OK，实际转化为s.get_score()
#s1.score = 999


class Student3(object):

	@property
	def birth(self):
		return self._birth

	@birth.setter
	def birth(self, value):
		self._birth = value

	@property
	def age(self):
		return 2017 - self._birth

s3 = Student3()
s3.birth = 1986
print(s3.birth, s3.age)

class Screen(object):

	@property
	def width(self):
		return self._width

	@width.setter
	def width(self, value1):
		self._width = value1

	@property
	def height(self):
		return self._height

	@height.setter
	def height(self, value2):
		self._height = value2

	@property
	def resolution(self):
		return self._width * self._height

s4 = Screen()
s4.width = 1024
s4.height = 768
print(s4.resolution)
assert s4.resolution == 786432, '1024 * 768 = %d ?' % s4.resolution
#assert的异常参数，其实就是在断言表达式后添加字符串信息，用来解释断言并更好的知道是哪里出了问题。