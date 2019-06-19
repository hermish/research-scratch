import matplotlib.pyplot as plt

# Note 0
def sigma(function, values):
	return sum(function(value) for value in values)

def pi(function, values):
	product = 1
	for image in (function(value) for value in values):
		product *= image
	return product

# Note 3
def recursive_fibonnaci(n):
	if n == 0 or n == 1:
		return n
	else:
		return recursive_fibonnaci(n - 1) + \
			recursive_fibonnaci(n - 2)

def iterative_fibonacci(n):
	if n == 0:
		return n
	head, runner = 1, 0
	for index in range(n - 1):
		head, runner = head + runner, head
	return head

def search(sorted_list, value):
	# Helper function defined
	def subsearch(sorted_list, value, start, end):
		# Base case
		if start == end:
			return -1
		# Recusive step
		midpoint = (start + end) // 2
		test = sorted_list[midpoint]
		if (value > test):
			return subsearch(sorted_list, value, midpoint + 1, end)
		elif (value < test):
			return subsearch(sorted_list, value, start, midpoint)
		# Base case
		else:
			return midpoint
	# Calling the helper function
	return subsearch(sorted_list, value, 0, len(sorted_list))

# Note 4
def stable_marriage(men, women, count=False):
	def terminate(saves):
		for woman in saves:
			if saves[woman] is None:
				return False
		return True

	def ask(man, woman, asks):
		asks[woman].append(man)

	def choose(woman, choices):
		if len(choices):
			rankings = [women[woman].index(choice) for choice in choices]
			max_ranking = max(rankings)
			index = rankings.index(max_ranking)
			preferred = choices[index]
			saves[woman] = preferred

	def iterate(saves):
		asks = dict((woman, []) for woman in women)
		for man in men:
			preferred = men[man][-1]
			ask(man, preferred, asks)
		for woman in women:
			choices = asks[woman]
			choose(woman, choices)			
		for man in men:
			preferred = men[man][-1]
			if saves[preferred] != man:
				men[man].pop()

	saves = dict((woman, None) for woman in women)
	iterations = 0
	while not terminate(saves):
		iterations += 1
		iterate(saves)
	return iterations if count else saves

def gcd(larger, smaller):
	if not smaller:
		return larger
	else:
		larger, smaller = smaller, larger % smaller
		return gcd(larger, smaller)

def extended_gcd(larger, smaller):
	if not smaller:
		return (larger, 1, 0)
	else:
		gcd, large, small = extended_gcd(smaller, larger % smaller)
		return (gcd, small, large - (larger // smaller) * small)

def inverse(number, prime):
	_, _, inverse = extended_gcd(prime, number)
	standarized = inverse % prime
	return standarized

def integrate(function, start, end, depth):
	"""
	:param function: A function which takes an float and returns a single float.
	:param start: The left-hand endpoints as either a float or integer.
	:param end: The right-hand endpoints as either a float or integer.
	:param depth: The number of intervals to based the estimation on.
	:return: (float) The signed area under the curve.
	"""
	over_sum = 0.0
	length = (end - start) / depth
	for index in range(depth):
		point = start + index * length
		over_sum += function(point) * length
	over_sum -= function(end) * length / 2
	over_sum -= function(start) * length / 2
	return over_sum

def long_stable_marriage(people):
	"""
	:param people: an integer which specifies the number of men and women
	returns a paried list of preference lists which ensure the stable
	marriage algorithm takes at least people ** 2 / 2 steps 
	"""
	individuals = range(people)
	men = []
	for person in range(people):
		men.append([0 if (rank == people) else 
			((person + rank - 1) % (people - 1)) + 1 
			for rank in range(people, 0, -1)])
	women = []
	for person in range(people):
		women.append([(person + rank - 1) % people
			for rank in range(people, 0, -1)])

	return dict(zip(individuals, men)), dict(zip(individuals, women))
	# return dict(zip(individuals, men)), dict(zip(individuals, women))
