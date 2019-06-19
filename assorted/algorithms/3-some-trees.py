class BinaryTree:
	"""
	An implementation of a BinaryTree which does not store parent information as
	an attribute. Notice the left and right branches are None unless explicitly
	specified.
	"""

	def __init__(self, label=None, left=None, right=None):
		self.label = label
		if not self.is_null():
			self.left = BinaryTree() if left is None else left
			self.right = BinaryTree() if right is None else right

	@classmethod
	def from_heap(cls, heap, start=0):
		size = len(heap)
		left, right = 2 * start + 1, 2 * start + 2
		if left < size and right < size:
			return cls(heap[start],
				cls.from_heap(heap, left),
				cls.from_heap(heap, right))
		if left < size:
			return cls(heap[start],
				cls.from_heap(heap, left))
		return cls(heap[start])

	def is_null(self):
		return self.label is None

	def is_leaf(self):
		return (self.label is not None and
			self.left.is_null() and self.right.is_null())

	def maximum(self):
		if self.right.is_null():
			return self.label
		return self.right.maximum()

	def minimum(self):
		if self.left.is_null():
			return self.label
		return self.left.minimum()

	def traversal(self):
		if self.is_null():
			return []
		middle = [self.label]
		return self.left.traversal() + middle + self.right.traversal()

	def insert(self, value):
		if self.is_null():
			self.label = value
			self.left, self.right = type(self)(), type(self)()
		elif value > self.label:
			self.right.insert(value)
		else:
			self.left.insert(value)

	def extend(self, iterable):
		for value in iterable:
			self.insert(value)
			# print(self)
			# print('---------')

	def _string_helper(self, indent):
		if self.is_null():
			return '\t' * indent + '*'
		label = '\t' * indent + str(self.label)
		if self.is_leaf():
			return label
		left_side = self.left._string_helper(indent + 1)
		right_side = self.right._string_helper(indent + 1)
		return right_side + '\n' + label + '\n' + left_side

	def __repr__(self):
		return self._string_helper(0)


class AVLTree(BinaryTree):
	"""
	An implementation of an AVL Tree, which is a formed of (reasonably well)
	balanced BinaryTree by ensuring that the difference in heghts between
	children nodes is always in the range [-1, 0, 1]. This allows the height
	of the tree to remain in the logarithm of its input size, which allows
	for a reasonable fast implementation of the priority queue Abstract
	Data Type
	"""
	def __init__(self, label=None, left=None, right=None):
		self.label = label
		self.height = -1
		if not self.is_null():
			self.left = AVLTree() if left is None else left
			self.right = AVLTree() if right is None else right
			self.height = max(self.right.height, self.left.height) + 1

	def height_difference(self):
		return self.right.height - self.left.height

	def is_left_heavy(self):
		return not self.is_null() and self.left.height > self.right.height

	def is_right_heavy(self):
		return not self.is_null() and self.right.height > self.left.height

	def right_rotate(self):
		self.right, self.left.left = self.left.left, self.right
		self.left.left, self.left.right = self.left.right, self.left.left
		self.left, self.right = self.right, self.left
		self.label, self.right.label = self.right.label, self.label

	def left_rotate(self):
		self.left, self.right.right = self.right.right, self.left
		self.right.left, self.right.right = self.right.right, self.right.left
		self.left, self.right = self.right, self.left
		self.label, self.left.label = self.left.label, self.label

	def insert(self, value):
		super().insert(value)
		self.height = max(self.right.height, self.left.height) + 1
		self.fix_avl_property()

	def fix_avl_property(self):
		if not self.is_null():
			if self.height_difference() > 1:
				self.left.fix_avl_property()
				self.right.fix_avl_property()
				if not self.right.is_left_heavy():
					self.left_rotate()
				else:
					self.right.right_rotate()
					self.left_rotate()
			elif self.height_difference() < -1:
				self.left.fix_avl_property()
				self.right.fix_avl_property()
				if not self.right.is_right_heavy():
					self.right_rotate()
				else:
					self.left.left_rotate()
					self.right_rotate()


def avl_sort(lst):
	"""
	Sorts LST using the avl sort algorithm
	+ Runtime: O(n log n) for time
	+ Runtime: O(n) for space
	
	>>> lst = [21, 5, 6, 7]
	>>> avl_sort(lst, 0, len(lst))
	[5, 6, 7, 21]
	"""
	avl_representation = AVLTree()
	avl_representation.extend(lst)
	return avl_representation.traversal()

