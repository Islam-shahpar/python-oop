#!/usr/bin/env python

#How to create a class?

class MyClass:
	x = 5

print(MyClass)

#How to create a class with methods and attributes?

class Person:
	def __init__(self, name, age):
		self.name = name
		self.age = age

	def sayName(self):
		print(f'My name is {self.name}')


#Instanciate an object

newPerson = Person("Shahpar", 28)

print(f'{newPerson.name} is {newPerson.age} years old')
	
