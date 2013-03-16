from random import random

def say_hello(name):
	print("Hello,","Would you like some hot chocolate?"
		if name in ("tom","Thomas","Tom","Thomas Wright")
		else "good evening.")

if __name__ == '__main__':
	say_hello(input("What is your name? "))

def are_you_yoda():
	yoda_or_doctor = input("Are you Yoda or the Doctor? ")
	if yoda_or_doctor in ("Yoda", "Yes I am Yoda",
		"May the force be with you."):
		print("Aren't you dead?")
	elif yoda_or_doctor == "The doctor":
		print("Doctor Who?" if random() < 0.3
			else "Would you like a jelly baby?")
	else:
		print("Meh, use the function properly!")


def how_old_are_you(age):
	if age < 0:
		print("stop messing around with this function")
	elif age > 900:
		are_you_yoda()
	else:
		print("hello normal person")

# #if __name__ == '__main__':
# 	how_old_are_you(int(input("How old are you? ")))
# 	#how_old_are_you(input("How old are you? "))

def factorial(n):
	''' Compute the factorial of a non-negative integer.
	>>> factorial(4)
	24
	>>> factorial(0)
	1
	>>> factorial(-1)
	Traceback (most recent call last):
	...
	ValueError: n must be a non-negative integer!
	'''
	if not isinstance(n, int) or n < 0:
		raise ValueError("n must be a non-negative integer!")
	return 1 if n == 0 else n * factorial(n - 1)