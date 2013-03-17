from functools import reduce
from numbers import Number
from vectors import Vector

class Matrix(object):
	def __init__(self, xss):
		'''
		>>> Matrix('Tom is purring')
		Traceback (most recent call last):
		...
		ValueError: This is not a matrix of numbers!
		>>> Matrix(['Tom is beautiful on weekdays','Tom is beautiful on weekends'])
		Traceback (most recent call last):
		...
		ValueError: This is not a matrix of numbers!
		>>> Matrix([[1],[1,2]])
		Traceback (most recent call last):
		...
		ValueError: This is not a matrix of numbers!
		'''
		if (not isinstance(xss, list)
			or not all(isinstance(xs, list) for xs in xss)
			or len(xss) == 0
			or len(xss[0]) == 0
			or reduce(lambda n, m: n if n == m else None,
				map(len, xss)) == None
			or not all(all(isinstance(x, Number) for x in xs)
				for xs in xss)):
			raise ValueError('This is not a matrix of numbers!')
		self.xss = [[complex(x) for x in xs] for xs in xss]

	def __repr__(self):
		''' Returns the representation of the object
		>>> Matrix([[1, 2], [3, 4]])
		Matrix([[(1+0j), (2+0j)], [(3+0j), (4+0j)]])
		'''
		return 'Matrix({})'.format(repr(self.xss))

	def __eq__(self, other):
		''' Are two matrices equal?
		>>> Matrix([[1, 2], [3, 4]]) == Matrix([[1, 2], [3, 4]])
		True
		>>> Matrix([[1, 2], [3, 4]]) == Matrix([[1, 2], [4, 4]])
		False
		>>> Matrix([[1], [2]]) == Matrix([[1, 2]])
		False
		>>> Matrix([[1, 2], [3, 4]]) == 'Juliet deserves a nice meal'
		False
		'''
		if isinstance(other, Matrix):
			return (self.order() == other.order()
				and all(xs == ys for (xs, ys) in zip(self, other)))
		return NotImplemented

	def __neg__(self):
		''' Negate a matrix.
		>>> - Matrix([[1, 2], [-3, 4]])
		Matrix([[(-1+0j), (-2+0j)], [(3+0j), (-4+0j)]])
		'''
		pass

	def __add__(self, other):
		''' Add two Matrices.
		>>> Matrix([[1, 2], [3, 4]]) + Matrix([[5, 6], [7, 8]])
		Matrix([[(6+0j), (8+0j)], [(10+0j), (12+0j)]])
		>>> Matrix([[1, 2]]) + Matrix([[3], [4]])
		Traceback (most recent call first):
		...
		ValueError: These matrices are not of the same order!
		>>> Matrix([[1, 2]]) + 'Juliet is beautiful'
		Traceback (most recent call first):
		...
		TypeError: unsupported operand type(s) for -: 'Matrix' and 'str'
		'''
		pass
	__radd__ = __add__

	def __sub__(self, other):
		''' Subtract one matrix from another.
		>>> Matrix([[1, 2], [3, 4]]) - Matrix([[1, 1], [1, 1]])
		Matrix([[(0+0j), (1+0j)], [(2+0j), (3+0j)]])
		'''
		pass

	def transpose(self):
		''' Swap the rows of the matrix with columns and vis versa.
		>>> Matrix([[1, 2], [3, 4]]).transpose()
		Matrix([[(1+0j), (3+0j)], [(2+0j), (4+0j)]])
		>>> Matrix([[1, 2, 3], [4, 5, 6]]).transpose()
		Matrix([[(1+0j), (4+0j)], [(2+0j), (5+0j)], [(3+0j), (6+0j)]])
		'''
		return Matrix(list(map(list, zip(*self))))

	def order(self, component = None):
		''' The order of the Matrix.
		>>> Matrix([[1, 2], [3, 4]]).order()
		(2, 2)
		>>> Matrix([[1, 2, 3], [4, 5, 6]]).order()
		(2, 3)
		'''
		(n, m) = (len(self.xss), len(self[1]))
		if component == 'n':
			return n
		if component == 'm':
			return m
		if component == None:
			return (n, m)

	def is_square(self):
		''' Is this a square matrix?
		>>> Matrix([[1, 2], [3, 4]]).is_square()
		True
		>>> Matrix([[1, 2, 3], [4, 5, 6]]).is_square()
		False
		'''
		return self.order('n') == self.order('m')

	def is_symmetric(self):
		''' Is this a symmetric matrix?
		>>> Matrix([[1, 2], [3, 4]]).is_symmetric()
		False
		>>> Matrix([[1, 2], [2, 3]]).is_symmetric()
		True
		'''
		return self == self.transpose()

	def is_antisymmetric(self):
		''' Is this an antisymmetric matrix?
		>>> Matrix([[1, 2], [3, 4]]).is_antisymmetric()
		False
		>>> Matrix([[0, 2], [-2, 0]]).is_antisymmetric()
		True
		'''
		pass

	def is_invertible(self):
		''' Is this an invertible matrix?
		>>> Matrix([[1, 2], [3, 4]]).is_invertible()
		True
		>>> Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]]).is_invertible()
		False
		'''
		pass

	def __getitem__(self, i):
		''' Get the ith row of the matrix as a vector.
		>>> Matrix([[1, 2], [3, 4]])[1]
		Vector((1+0j), (2+0j))
		>>> Matrix([[1, 2], [3, 4]])[2][1]
		(3+0j)
		'''
		return Vector(*self.xss[i - 1])

	def __iter__(self):
		for xs in self.xss:
			yield Vector(*xs)

	def minor(self, i, j):
		''' Get the i j minor of the matrix.
		>>> Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]]).minor(2, 2)
		Matrix([[(1+0j), (3+0j)], [(7+0j), (9+0j)]])
		'''
		return Matrix([[x for (m, x) in enumerate(xs, 1) if m != j]
			for (l, xs) in enumerate(self, 1) if l != i])

	def trace(self):
		''' Get the trace of the matrix.
		>>> Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]]).trace()
		(15+0j)
		'''
		return sum(self[i][i] for i in range(1, self.order('m') + 1))

	def det(self):
		''' Get the determinant of the matrix.
		>>> Matrix([[1, 2], [3, 4]]).det()
		(-2+0j)
		>>> Matrix([[1], [1], [1]]).det()
		Traceback (most recent call last):
		...
		ValueError: Determinant is only defined for square matrices.
		'''
		if not self.is_square():
			raise ValueError('Determinant is only defined for square matrices.')
		if self.order() == (1, 1):
			return self[1][1]
		return sum(((-1)**(j + 1))*x*self.minor(1, j).det() for (j, x)
			in enumerate(self[1], 1))

	def charactoristic_polynomial(self, variable):
		''' Get the charactoristic polynomial of the Matrix.
		>>> Matrix([[1, 2], [3, 4]]).charactoristic_polynomial(Variable('x'))
		Polynomial('x', (-2+0j), (-5+0j), (1+0j))
		'''
		pass