class Chain(object):
	def __init__(self, path=''):
		self._path = path

	def __getattr__(self, path):
		return Chain('%s/%s' % (self._path, path))

	def __str__(self):
		return self._path

	__repr__ = __str__


print(Chain().status.user.timeline.list)

class Student(object):
	def __init__(self, name='111'):
		self._name = name

	def __getattr__(self, attr):
		if attr=='score':
			return 99
		elif attr=='age':
			return lambda:25

	def __call__(self):
		print('My name is %s' % self._name)


s = Student('Michael')
print(s._name)
print(s.score)
print(s.age())
s()

print(callable(s))
print(callable(Student('b')))
print(callable(max))
print(callable('str'))
print(callable(Student))
Student()