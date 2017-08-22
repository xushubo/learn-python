class Animal(object):
	pass
a = Animal()

print(type(123))
print(type('str'))
print(type(None))
print(type(abs))
print(type(a))

print(type(123)==type(456))
print(type(123)==int)
print(type('abc')==type('123'))
print(type('abc')==str)
print(type('abc')==type(123))

import types
def fn():
	pass

print(type(fn)==types.FunctionType)
print(type(abs)==types.BuiltinFunctionType)
print(type(lambda x: x)==types.LambdaType)
print(type(x for x in range(10))==types.GeneratorType)

class Dog(Animal):
	pass

class Husky(Dog):
	pass

d = Dog()
h = Husky()

print(isinstance(h, Husky))
print(isinstance(h, Dog))
print(isinstance(h, Animal))

print(isinstance(d, Dog) and isinstance(d, Animal))
print(isinstance(d, Husky))

print(isinstance(123, int))
print(isinstance('a', str))
print(isinstance(b'a', bytes))

print(isinstance([1, 2, 3], (list, tuple)))
print(isinstance((1, 2, 3), (list, tuple)))

print(dir('abc'))
print('abc'.__dir__())
print(len('ABC'))
print('ABC'.__len__())

class MyDog(object):
	def __len__(self):
		return 100

dog = MyDog()
print(len(dog))

class MyObiect(object):
	def __init__(self):
		self.x = 9
	def power(self):
		return self.x * self.x

obj = MyObiect()

print(hasattr(obj, 'x'))
print(obj.x)
print(hasattr(obj, 'y'))
setattr(obj, 'y', 19)
print(hasattr(obj, 'y'))
print(getattr(obj, 'y'))
print(obj.y)
print(getattr(obj, 'z', 404)) # 获取属性'z'，如果不存在，返回默认值404

print(hasattr(obj, 'power'))
print(getattr(obj, 'power'))
fn = getattr(obj, 'power')
print(fn)
print(fn())
