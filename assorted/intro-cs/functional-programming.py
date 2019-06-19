class Pair:
	def __init__(self, first, second):
		def func(index):
			return second if index else first
		self.pair = func

	def __getitem__(self, key):
		return self.pair(key)

	def __setitem__(self, key, value):
		first = value if not key else self[0]
		second = value if key else self[1]
		self.pair = Pair(first, second).pair

	def __repr__(self):
		return '(' + repr(self[0]) + ', ' + \
			repr(self[1]) + ')'

class Array:
	def __init__(self, first, rest):
		self.store = Pair(first, rest)

	def __len__(self):
		return 1 if self.rest() is None \
			else 1 + len(self.rest())

	def __getitem__(self, key):
		assert key < len(self)
		return self.rest()[key - 1] if key else self.first()

	def __repr__(self):
		return repr(self.first()) if self.rest() is None \
                        else repr(self.first()) + ', ' + repr(self.rest())
	
	def first(self):
		return self.store[0]

	def rest(self):
		return self.store[1]
