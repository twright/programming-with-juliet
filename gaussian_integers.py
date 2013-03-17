class GaussianInteger(object):
	"""docstring for GaussianInteger"""
	def __init__(self, real, imag):
		self.real = int(real)
		self.imag = int(imag)

	## Need checks that indeed a GaussianInteger

	def __repr__(self):
		''' Returns the representation of the object.
		>>> GaussianInteger(2, 3)
		GaussianInteger(2, 3)
		'''
		return 'GaussianInteger({}, {})'.format(self.real, self.imag)

	def __str__(self):
		''' Returns the object as a string.
		>>> str(GaussianInteger(2, 3))
		'2 + 3i'
		>>> str(GaussianInteger(0, 3))
		'3i'
		>>> str(GaussianInteger(2, 0))
		'2'
		>>> str(GaussianInteger(0, 0))
		'0'
		>>> str(GaussianInteger(-2, -3))
		'-2 - 3i'
		>>> str(GaussianInteger(2, -3))
		'2 - 3i'
		>>> str(GaussianInteger(-2, 3))
		'-2 + 3i'
		>>> str(GaussianInteger(0, -3))
		'-3i'
		>>> str(GaussianInteger(-2, 0))
		'-2'
		'''
		if self.real == self.imag == 0:
			return '0'
		if self.real == 0:
			return str(self.imag) + 'i'
		if self.imag == 0:
			return str(self.real)
		if self.imag < 0:
			return '{} - {}i'.format(self.real, abs(self.imag))
		return '{} + {}i'.format(self.real, self.imag)

	def conjugate(self):
		''' Finding the conjugate of the GaussianInteger so given
		GaussianInteger(a,b) returns GaussianInteger(a,-b).
		>>> GaussianInteger(2,3).conjugate()
		GaussianInteger(2, -3)
		'''
		return GaussianInteger(self.real, -self.imag)

	def __neg__(self):
		''' Finding the additive inverse of a GaussianInteger.
		>>> -GaussianInteger(2, -3)
		GaussianInteger(-2, 3)
		'''
		return GaussianInteger(-self.real, -self.imag)

	def __eq__(self, other):
		''' Finding if two GaussianIntegers are equal.
		>>> GaussianInteger(-2, 3) == GaussianInteger(-2, 3)
		True
		>>> GaussianInteger(-2, 4) == GaussianInteger(-2, 3)
		False
		>>> GaussianInteger(-1, 3) == GaussianInteger(-2, 3)
		False
		>>> GaussianInteger(-1, 4) == GaussianInteger(5, 6)
		False
		>>> 4 == GaussianInteger(4, 0)
		True
		>>> GaussianInteger(4, 0) == 4
		True
		'''
		if isinstance(other, int):
			return self == GaussianInteger(other, 0)
		if isinstance(other, GaussianInteger):
			return self.real == other.real and self.imag == other.imag
		return NotImplemented

	def __add__(self, other):
		''' Adds two GaussianIntegers.
		>>> GaussianInteger(2, 3) + GaussianInteger(-3, 5)
		GaussianInteger(-1, 8)
		>>> GaussianInteger(-3, 5) + GaussianInteger(2, 3)
		GaussianInteger(-1, 8)
		>>> GaussianInteger(2, 3) + 4
		GaussianInteger(6, 3)
		>>> 4 + GaussianInteger(2, 3)
		GaussianInteger(6, 3)
		>>> GaussianInteger(2, 3) + 'Juliet it beautiful'
		Traceback (most recent call last):
		...
		TypeError: unsupported operand type(s) for +: 'GaussianInteger' and 'str'
		>>> 'Juliet it beautiful' + GaussianInteger(2, 3)
		Traceback (most recent call last):
		...
		TypeError: Can't convert 'GaussianInteger' object to str implicitly
		'''
		if isinstance(other, int):
			return self + GaussianInteger(other, 0)
			#GaussianInteger(self.real + other, self.imag)
		if isinstance(other, GaussianInteger):
			return GaussianInteger(self.real + other.real,
				self.imag + other.imag)
		return NotImplemented
	__radd__ = __add__

	def __sub__(self, other):
		''' Subtracts a GaussianInteger or int from another GaussianInteger.
		>>> GaussianInteger(-4, 3) - GaussianInteger(5, -4)
		GaussianInteger(-9, 7)
		>>> GaussianInteger(-4, 3) - 4
		GaussianInteger(-8, 3)
		>>> GaussianInteger(1, -1) - 'tom is tired'
		Traceback (most recent call last):
		...
		TypeError: unsupported operand type(s) for -: 'GaussianInteger' and 'str'
		'''
		if isinstance(other, (int, GaussianInteger)):
			return self + -other
		return NotImplemented

	def __rsub__(self, other):
		'''
		>>> 4 - GaussianInteger(-4, 3)
		GaussianInteger(8, -3)
		>>> 'tom is lovely' - GaussianInteger(1, -1)
		Traceback (most recent call last):
		...
		TypeError: unsupported operand type(s) for -: 'str' and 'GaussianInteger'
		'''
		if isinstance(other, (int, GaussianInteger)):
			return -self + other
		return NotImplemented

	def __mul__(self, other):
		''' Multiplies two GaussianIntegers so
		GaussianInteger(a,b)*GaussianInteger(c,d)
		= GaussianInteger(ac - bd, ad + bc).
		>>> GaussianInteger(2,3)*GaussianInteger(4,5)
		GaussianInteger(-7, 22)
		>>> GaussianInteger(4,5)*GaussianInteger(2,3)
		GaussianInteger(-7, 22)
		>>> GaussianInteger(2, 3)*4
		GaussianInteger(8, 12)
		>>> 4*GaussianInteger(2, 3)
		GaussianInteger(8, 12)
		>>> GaussianInteger(2, 3)*'Tom is still lovely'
		Traceback (most recent call last):
		...
		TypeError: can't multiply sequence by non-int of type 'GaussianInteger'
		>>> 'Tom is lovely'*GaussianInteger(2,3)
		Traceback (most recent call last):
		...
		TypeError: can't multiply sequence by non-int of type 'GaussianInteger'
		'''
		if isinstance(other, int):
			return self * GaussianInteger(other, 0)
			#GaussianInteger(self.real*other, self.imag*other)
		if isinstance(other, GaussianInteger):
			return GaussianInteger(self.real*other.real - self.imag*other.imag,
				self.real*other.imag + self.imag*other.real)
		return NotImplemented
	__rmul__ = __mul__

	def __abs__(self):
		''' Finds the norm of a GaussianInteger so abs(GaussianInteger(a, b))
		= a**2 + b**2
		>>> abs(GaussianInteger(2, -3))
		13
		'''
		return self.real**2 + self.imag**2

	def __divmod__(self, other):
		''' Implement the division algorithm for GaussianIntegers and
		returns a tuple (q, r) with q the quotient GaussianInteger and
		r the remainder GaussianInteger.
		>>> divmod(GaussianInteger(2, 3), GaussianInteger(0, 0))
		Traceback (most recent call last):
		...
		ZeroDivisionError: GaussianInteger division or modulo by zero
		>>> divmod(GaussianInteger(0, 0), GaussianInteger(2, 3))
		(GaussianInteger(0, 0), GaussianInteger(0, 0))
		>>> divmod(GaussianInteger(-5, 10), GaussianInteger(3, 4))
		(GaussianInteger(1, 2), GaussianInteger(0, 0))
		>>> divmod(GaussianInteger(-4, 11), GaussianInteger(3, 4))
		(GaussianInteger(1, 2), GaussianInteger(1, 1))
		>>> divmod(GaussianInteger(12, 16), 4)
		(GaussianInteger(3, 4), GaussianInteger(0, 0))
		>>> divmod(GaussianInteger(13, 18), 4)
		(GaussianInteger(3, 4), GaussianInteger(1, 2))
		>>> divmod(GaussianInteger(3, 4), 'Tom is very cuddly')
		Traceback (most recent call last):
		...
		TypeError: unsupported operand type(s) for divmod(): 'GaussianInteger' and 'str'
		'''
		if other == 0:
			raise ZeroDivisionError(
				'GaussianInteger division or modulo by zero')

		if isinstance(other, int):
			return divmod(self, GaussianInteger(other, 0))

		if isinstance(other, GaussianInteger):
			re = round((self.real*other.real + self.imag*other.imag)
				/ abs(other))
			im = round((self.imag*other.real - self.real*other.imag)
				/ abs(other))
			q = GaussianInteger(re, im)
			r = self - other*q
			return (q, r)

		return NotImplemented


	def __rdivmod__(self, other):
		'''
		>>> divmod(5, GaussianInteger(1, 2))
		(GaussianInteger(1, -2), GaussianInteger(0, 0))
		>>> divmod(5, GaussianInteger(0, 0))
		Traceback (most recent call last):
		...
		ZeroDivisionError: GaussianInteger division or modulo by zero
		>>> divmod('Tom is very cuddly', GaussianInteger(3, 4))
		Traceback (most recent call last):
		...
		TypeError: unsupported operand type(s) for divmod(): 'str' and 'GaussianInteger'
		'''
		if isinstance(other, int):
			return GaussianInteger(other, 0).__divmod__(self)
		return NotImplelmented