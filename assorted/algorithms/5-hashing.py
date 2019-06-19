import math
from collections import deque
import primesieve
import random

class LinkedList:
	"""
	Implements a simple linked list class, where each LIST object consists of a
	first element and a rest. This implements through Python's collections
	iterface: providing length, contains, getitem, setitem and iter methods.
	"""
	nil = None

	def __init__(self, first, rest=nil):
		self.first = first
		self.rest = rest

	def __repr__(self):
		return '<' + ', '.join(map(repr, self)) + '>'

	def __iter__(self):
		current = self
		while current is not LinkedList.nil:
			yield current.first
			current = current.rest

	def __contains__(self, value):
		current = self
		while current is not LinkedList.nil:
			if current.first == value:
				return True
			current = current.rest
		return False

	def __getitem__(self, index):
		current = self
		while current is not LinkedList.nil:
			if not index:
				return current.first
			index -= 1
			current = current.rest
		raise IndexError

	def __setitem__(self, index, value):
		current = self
		while current is not LinkedList.nil:
			if not index:
				current.first = value
			index -= 1
			current = current.rest
		raise IndexError

	def __len__(self):
		current, length = self, 0
		while current is not LinkedList.nil:
			length += 1
			current = current.rest
		return length

	def replace(self, old, new):
		current = self
		while current is not LinkedList.nil:
			if current.first == old:
				current.first = new
			current = current.rest

	def remove_inside(self, value):
		current = self
		while current.rest is not LinkedList.nil: 
			if current.rest.first == value:
				current.rest = current.rest.rest
			current = current.rest


class ChainMultiSet:
	"""
	Implments a multiset using a simple hash function, using to chaining to deal
	with collisions. Notice we use python own __hash__ function to pre-hash
	objects to deal with 
	"""
	default_size = 8

	def __init__(self):
		self.table_size = self.default_size
		self.table = [LinkedList.nil for _ in range(self.table_size)]
		self.length = 0
		self.hash_func = self._get_division_hash(self.default_size)

	def __repr__(self):
		return '{' + ', '.join(map(repr, self)) + '}'

	def __iter__(self):
		for chain in self.table:
			if chain is not LinkedList.nil:
				for entry in chain:
					yield entry

	def __len__(self):
		return self.length

	def __contains__(self, value):
		pos = self.hash_func(value)
		return self.table[pos] is not LinkedList.nil and \
			value in self.table[pos]

	@property
	def load(self):
		return self.length / self.table_size

	@classmethod
	def from_list(cls, lst):
		chain_set = cls()
		chain_set.extend(lst)
		return chain_set

	def insert(self, value):
		self.length += 1
		if self.length > self.table_size:
			self._double()
		pos = self.hash_func(value)
		self.table[pos] = LinkedList(value, self.table[pos])

	def extend(self, values):
		for value in values:
			self.insert(value)

	@staticmethod
	def _get_division_hash(table_size):
		# Pre-hashes using Python's built-in function
		# Gotta love those function closures which make it possible to just
		# use self.table_size and have it automatically update; using this
		# forces changing the hash function to be more explicit in, for example,
		# table doubling
		return lambda x: hash(x) % table_size

	def _double(self):
		new_size = 2 * self.table_size
		new_table = [LinkedList.nil for _ in range(new_size)]
		new_hash = self._get_division_hash(new_size)
		for value in self:
			pos = new_hash(value)
			new_table[pos] = LinkedList(value, new_table[pos])
		self.table_size = new_size
		self.table = new_table
		self.hash_func = new_hash


class ChainSet(ChainMultiSet):
	"""
	A class represting a HashSet in python with O(1) amortized run-time with 
	high probability for insertions and deletions, along with O(1) run-times 
	for exact search. Unless the CHAINMULTISET class, this set class does not
	allow for equality.
	"""
	def insert(self, value):
		if value not in self:
			super().insert(value)
		else:
			pos = self.hash_func(value)
			self.table[pos].replace(value, value)

	def delete(self, value):
		pos = self.hash_func(value)
		if len(self.table[pos]) > 1:
			self.table[pos].remove_inside(value)
		else:
			self.table[pos] = LinkedList.nil


class RollingCharHash:
	"""
	A rolling hash object which uses a linear hash function over a sequence of
	characters. It supports basic operations of adding and removing characters
	as well as equality checking. Uses a deque to store current characters in
	memory.
	"""
	def __init__(self, prime=None):
		self.hash_value = 0
		self.prime = prime if prime is None else self._get_prime()
		self.buffer = deque()

	@staticmethod
	def _get_prime():
		lowest = random.randint(10000, 100000) 
		return primesieve.nth_prime(lowest)

	def add(self, char):
		new_val = self.hash_value * 256 + ord(char)
		self.hash_value = new_val % self.prime
		self.buffer.append(char)

	def add_word(self, chars):
		for char in chars:
			self.add(char)

	def clear(self):
		self.hash_value = 0
		self.buffer = deque()

	def remove(self):
		first = self.buffer.popleft()
		to_sub = pow(256, len(self.buffer), self.prime) * ord(first)
		new_val = self.hash_value - to_sub
		self.hash_value = new_val % self.prime

	def equals_to(self, word, word_hash=None):
		if len(word) != len(self.buffer):
			return False
		if word_hash is None:
			word_roller = RollingCharHash(self.prime)
			word_roller.add_word(word)
			word_hash = word_roller.hash_value
		if word_hash != self.hash_value:
			return False
		return all(char1 == char2 for char1, char2 in 
			zip(word, self.buffer))

def rabin_karp(word, document):
	"""
	Checks whether or not WORD is a substring of DOCUMENT, using the rabin_karp
	algorithm with runtime O(|word| + |document|). Returns a boolean True or
	False depending on whether or not the word is present.
	"""
	rolling_hash = RollingCharHash()
	rolling_hash.add_word(word)
	to_match = rolling_hash.hash_value
	rolling_hash.clear()

	rolling_hash.add_word(document[0:len(word)])
	if rolling_hash.equals_to(word, to_match):
		return False
	for pos in range(len(word), len(document)):
		rolling_hash.remove()
		rolling_hash.add(document[pos])
		if rolling_hash.equals_to(word, to_match):
			return True
	return False

