def naive_counting_sort(int_lst, bins):
	"""
	Sorts INT_LST using the naive counting sort algorithm, given that all
	elements are in elemet in the range [0, 1, ... BINS - 1].
	+ Runtime: O(n + k) where k is the number of bins and n the number of
		of elemets to be sorted
	"""
	buckets = [0] * bins
	for value in int_lst:
		buckets[value] += 1
	output = []
	for value in range(bins):
		for number in range(buckets[value]):
			output.append(value)
	return output


def counting_sort(lst, key, bins):
	"""
	Sorts LAST using the naive counting sort algorithm, given that all images
	of the KEY function are elements in the range [0, 1, ... BINS - 1].
	+ Runtime: O(n + k) where k is the number of bins and n the number of
		of elemets to be sorted
	"""
	buckets = [[] for _ in range(bins)]
	for item in lst:
		print('\t', item)
		value = key(item)
		buckets[value].append(item)
	
	return [x for bucket in buckets for x in bucket]


def radix_sort(lst, base=10):
	"""
	Sorts LST and returns a new list using the radix sort algorithm, operating
	in some base BASE; note, by default this is the 10.
	"""
	output = lst
	power = 1
	max_element = max(lst)
	while power <= max_element:
		key = lambda num: (num // power) % base
		output = counting_sort(output, key, base)
		power *= base
		print(output)
	return output
