class Expression(object):
	def roots(self, variable=None):
		pass

	def degree(self, variable=None):
		pass

	def expand():
		pass

	def is_poly(self, variable=None):
		pass

	def is_linear(self, variable=None):
		pass

class Variable(Expression):
	"""docstring for Variables"""
	def __init__(self, name):
		if isinstance(name, str):
			self.__name = name
		else:
			raise TypeError('name must be a string')

	@property
	def name(self):
		return self.__name

	def degree(self, variable=None):
		return 1 if self == variable else 0

	def expand(self):
		return self

	def is_poly(self, variable=None):
		return self == variable

	is_linear = is_poly

	def roots(self, variable=None):
		return {0} if self == variable else {}

	def __repr__(self):
		'''
		>>> Variable('x')
		Variable('x')
		'''
		return 'Variable({})'.format(self.name)

	def __call__(self, x, variable=None):
		return x if self == variable else self

	def __eq__(self, other):
		return other == None or self.name == other.name

class Product(Expression):
	"""docstring for Product"""
	def __init__(self, *xs):
		super(Product, self).__init__()
		self.arg = arg

class Power(Expression):
	"""docstring for Power"""
	def __init__(self, arg):
		super(Power, self).__init__()
		self.arg = arg

class Sum(Expression):
	"""docstring for Sum"""
	def __init__(self, arg):
		super(Sum, self).__init__()
		self.arg = arg

