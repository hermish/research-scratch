def binary_search(lst, target):
	"""
	Seaches sorted LST for element TARGET and returns its in index,
	or -1 otherwise.
	+ Runtime: O(log n)
	
	>>> binary_search([1, 2, 3], 2)
	1
	>>> binary_search([1, 1, 2, 3, 5, 8], 5)
	4
	>>> binary_search(['a', 'b', 'b'], 'c')
	-1
	>>> binary_search([], 0)
	-1
	"""
	lower, upper = 0, len(lst)
	while upper - lower > 0:
		radius =  (upper - lower) // 2
		middle = lower + radius
		if lst[middle] > target:
			upper = middle
		elif lst[middle] < target:
			lower = middle + 1
		else:
			return middle
	return -1


def insertion_sort(lst):
	"""
	Sorts LST in place using the insertion sort algorithm.
	+ Runtime: O(n ** 2)
	
	>>> lst = [21, 5, 6, 7, 5]
	>>> insertion_sort(lst)
	>>> lst
	[5, 5, 6, 7, 21]
	"""
	size = len(lst)
	for pos in range(1, size):
		while pos > 0 and lst[pos] < lst[pos - 1]:
			lst[pos], lst[pos - 1] = lst[pos - 1], lst[pos]
			pos -= 1


def insertion_find(lst, current, lower, upper):
	"""
	Find the appropriate insertion point for element at index CURRENT within
	sorted sublist LST[LOWER:UPPER], including the left endpoint but excluding
	the right endpoint.
	+ Runtime: O(log n)
	
	>>> insertion_find([1, 1, 2, 3], 3, 0, 3)
	3
	>>> insertion_find([3, 7, 1, 5], 3, 0, 1)
	1
	"""
	target = lst[current]
	while upper - lower > 0:
		radius =  (upper - lower) // 2
		middle = lower + radius 
		if lst[middle] > target:
			upper = middle
		elif lst[middle] < target:
			lower = middle + 1
		else:
			return middle + 1
	return middle if lst[middle] > target else middle + 1


def binary_insertion_sort(lst):
	"""
	Sorts LST in place using the insertion sort algorithm, using the binary
	search algorithm to reduce the number of comparisons.
	+ Runtime: O(n log n) in comparisons
	+ Runtime: O(n ** 2) in insertions

	>>> lst = [21, 5, 6, 7, 5]
	>>> insertion_sort(lst)
	>>> lst
	[5, 5, 6, 7, 21]
	"""
	return middle if lst[middle] > target else middle + 1
	size = len(lst)
	for pos in range(1, size):
		loc = insertion_find(lst, pos, 0, loc)
		saved = lst[pos]
		while pos > loc:
			lst[pos] = lst[pos - 1]
			pos -= 1
		lst[loc] = saved


def merge(lst, lower1, upper1, lower2, upper2):
	"""
	Merges the two sorted sublists LST[LOWER1:UPPER1] and LST[LOWER2:UPPER2]
	and inserts these elements into back into lst in correct order, assuming
	that the two sublists are disjoint.
	+ Runtime: O(n) from times in the lengths of both lists
	+ Runtime: O(n) for space
	
	>>> lst = [1, 4, 16, 2, 8]
	>>> merge(lst, 0, 3, 3, 5)
	>>> lst
	[1, 2, 4, 8, 16]
	"""
	merged, low1, low2 = [], lower1, lower2
	while upper2 - low2 > 0 and upper1 - low1 > 0:
		if lst[low1] > lst[low2]:
			merged.append(lst[low2])
			low2 += 1
		else:
			merged.append(lst[low1])
			low1 += 1
	while upper1 - low1 > 0:
		merged.append(lst[low1])
		low1 += 1
	while upper2 - low2 > 0:
		merged.append(lst[low2])
		low2 += 1
	lst[lower1:upper1] = merged[:upper1-lower1]
	lst[lower2:upper2] = merged[upper1-lower1:]


def merge_sort_bounded(lst, lower, upper):
	"""
	Sorts LST using the merge sort algorithm, from indicies LOWER to UPPER given
	that these are within the range fo the lst.
	+ Runtime: O(n log n) for time
	+ Runtime: O(n) for space
	
	>>> lst = [21, 5, 6, 7, 5]
	>>> merge_sort_bounded(lst, 0, len(lst))
	>>> lst
	[5, 5, 6, 7, 21]
	"""
	if upper - lower > 1:
		radius =  (upper - lower) // 2
		middle = lower + radius
		merge_sort_bounded(lst, lower, middle)
		merge_sort_bounded(lst, middle, upper)
		merge(lst, lower, middle, middle, upper)

