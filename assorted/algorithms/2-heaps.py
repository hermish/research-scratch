def build_max_heap(lst):
	"""
	Takes and array LST and returns a max heap.
	"""
	size = len(lst)
	for pos in reversed(range(size // 2)):
		max_heapify(lst, pos, size)


def max_heapify(lst, pos, bound):
	"""
	Corrects at most one violation of the heap property in a sub-tree's root,
	where LST is an array which contains the heap upto but not inclduing the
	elment at index BOUND, and POS is the index of a node which exibits this 
	potential violation. Notice that POS < BOUND.
	"""
	left = 2 * (pos + 1) - 1
	right = 2 * (pos + 1)
	if right < bound and lst[right] > lst[left] and lst[right] > lst[pos]:
		lst[pos], lst[right] = lst[right], lst[pos]
		max_heapify(lst, right, bound)
	elif left < bound and lst[left] > lst[pos]:
		lst[pos], lst[left] = lst[left], lst[pos]
		max_heapify(lst, left, bound)


def heap_sort(lst):
	"""
	Sorts the array LST using the heap sort algorithm.
	+ Runtime: O(n log n)

	>>> lst = [21, 5, 6, 7, 5]
	>>> heap_sort(lst)
	>>> lst
	[5, 5, 6, 7, 21]
	"""
	size = len(lst)
	build_max_heap(lst)
	for bound in reversed(range(size)):
		lst[0], lst[bound] = lst[bound], lst[0]
		max_heapify(lst, 0, bound)
