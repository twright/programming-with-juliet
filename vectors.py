class Vector(object):
	"""docstring for Vector"""
	def __init__(self, *xs):
		self.xs = list(map(complex, xs))

	def __repr__(self):
		'''
		>>> Vector(1, 2, 3)
		Vector((1+0j), (2+0j), (3+0j))
		'''
		return 'Vector({})'.format(', '.join(map(repr, self.xs)))

	def __len__(self):
		''' Returns the length of the Vector.
		>>> len(Vector(1, 2, 3))
		3
		'''
		return len(self.xs)

	def __eq__(self, other):
		''' Are two vectors equal?
		>>> Vector(1, 2) == Vector(1, 2)
		True
		>>> Vector(1, 2) == Vector(1, 3)
		False
		>>> Vector(1, 2) == Vector(3, 4, 5)
		False
		>>> Vector(1, 2) == 'Juliet is very pretty!'
		False
		'''
		if isinstance(other, Vector):
			return (len(self) == len(other)
				and all(x == y for (x, y) in zip(self, other)))
		return NotImplemented

	def __getitem__(self, i):
		''' Get the ith element of the Vector.
		>>> Vector(1, 2, 3)[2]
		(2+0j)
		'''
		return self.xs[i-1]

	def __iter__(self):
		for x in self.xs:
			yield x

	def __add__(self, other):
		'''
		>>> Vector(1, 2) + Vector(3, (1+2j))
		Vector((4+0j), (3+2j))
		>>> Vector(1, 2) + Vector(1)
		Traceback (most recent call last):
		...
		ValueError: can only add vectors of the same length
		>>> Vector(1, 2) + 'It was snowing today.'
		Traceback (most recent call last):
		...
		TypeError: unsupported operand type(s) for +: 'Vector' and 'str'
		'''
		if isinstance(other, Vector):
			if len(self) != len(other):
				raise ValueError('can only add vectors of the same length')
			#return Vector(*[self[i] + other[i] for i in
			#	range(1, len(self) + 1)])
			return Vector(*[x + y for (x, y) in zip(self, other)])
		return NotImplemented


	def __mul__(self, other):
		'''
		>>> Vector(2, 3) * (1+4j)
		Vector((2+8j), (3+12j))
		>>> Vector(1, 2) * Vector(3, 4)
		(11+0j)
		'''
		pass

	def __rmul__(self):
		'''
		>>> 2 * Vector(1, 2)
		Vector((2+0j), (4+0j))
		'''
		pass