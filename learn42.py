class Student(object):
	def __init__(self, name):
		self.name = name

	def __str__(self):
		return('Student object (name: %s)' % self.name)
	__repr__ = __str__

print(Student('Michael'))


class Fib(object):
	def __init__(self):
		self.a, self.b = 0, 1

	def __iter__(self):
		return self

	def __next__(self):
		self.a, self.b = self.b, self.a + self.b
		if self.a > 20:
			raise StopIteration()
		return self.a

	def __len__(self):
		return 7

	def __getitem__(self, n):
		if isinstance(n, int):
			for x in range(n + 1):
				self.a, self.b = self.b, self.a + self.b
			return self.a
		if isinstance(n, slice):
			start = n.start
			stop = n.stop
			step = n.step
			if start is None:
				start = 0
			if stop is None:
				stop = len(self)
			if start < 0:
				start = len(self) + start
			if stop < 0:
				stop = len(self) + stop
			if step is None:
				step = 1
			L = []
			if step > 0:
				a = 0
				for x in range(stop):
					self.a, self.b = self.b, self.a + self.b
					if x >= start:
						if a % step == 0:
							L.append(self.a)
						a = a + 1
				return L
#			if step < 0:


for n in Fib():
	print(n)

print(Fib()[5])
print(Fib()[0:5])
print(Fib()[:3])
print(Fib()[5:2])
print(Fib()[-1:3])
L = [1, 2, 3, 4, 5, 6, 7, 8]
print(L[-1:3])
print(L[-2:-1])
print(L[6:7])
print(L[::-1])
print(L[5:2])
print(L[:-1])
print(L[-6:6])
print(L[-1::-2])
print(Fib()[1:5:3])