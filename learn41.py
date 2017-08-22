class Animal(object):
	def run(self):
		print('animal is running...')

class Mammal(Animal):
	def run(self):
		print('mammal is running...')

class Bird(Animal):
	pass

class Dog(Mammal):
	pass

class Bat(Mammal):
	pass

class Parrot(Bird):
	pass

class Ostrich(Bird):
	pass

class Runnable(object):
	def run(self):
		print('runnable is running...')

class Flyable(object):
	def run(self):
		print('flyable is running...')

class Dog(Runnable, Mammal):
	pass

class Bat(Mammal, Flyable):
	pass

d = Dog()
b = Bat()

d.run()
b.run()

