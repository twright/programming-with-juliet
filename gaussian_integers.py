class GaussianInteger(object):
	"""docstring for GaussianInteger"""
	def __init__(self, real, imag):
		self.real = int(real)
		self.imag = int(imag)

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
		'''
		return self.real == other.real and self.imag == other.imag

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
			return GaussianInteger(self.real + other, self.imag)
		if isinstance(other, GaussianInteger):
			return GaussianInteger(self.real + other.real,
				self.imag + other.imag)
		return NotImplemented
		# raise TypeError(("unsupported operand type(s) for +: 'GaussianInteger' "
			# 	+ "and '{}'").format(other.__class__.__name__))
	__radd__ = __add__

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
		>>> GaussianInteger(2, 3)*'Tom is lovely'
		Traceback (most recent call last):
		...
		TypeError: can't multiply sequence by non-int of type 'GaussianInteger'
		>>> 'Tom is lovely'*GaussianInteger(2,3)
		Traceback (most recent call last):
		...
		TypeError: can't multiply sequence by non-int of type 'GaussianInteger'
		'''
		if isinstance(other, int):
			return GaussianInteger(self.real*other, self.imag*other)
		if isinstance(other, GaussianInteger):
			return GaussianInteger(self.real*other.real - self.imag*other.imag,
				self.real*other.imag + self.imag*other.real)
		return NotImplemented
	__rmul__ = __mul__

