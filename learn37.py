class Animal(object):
	def run(self):
		print('Animal is running...')

class Cat(Animal):
	def run(self):
		print('Cat is running...') #当子类和父类都存在相同的run()方法时，子类的run()覆盖了父类的run()

class Dog(Animal):
	def run(self):
		print('Dog is running...')

C = Cat()
D = Dog()
C.run()
D.run()

a = list() #a是list类型
b = Animal() #b是Animal类型
c = Dog() #c是Dog类型

print(isinstance(a, list))
print(isinstance(b, Animal))
print(isinstance(c, Dog))
print(isinstance(c, Animal))
print(isinstance(b, Dog))

def run_twice(animal):
	animal.run()
	animal.run()

run_twice(Animal())
run_twice(Cat())
run_twice(Dog())

class Tortoise(Animal):
	def run(self):
		print('Tortoise is running slowly...')

run_twice(Tortoise())