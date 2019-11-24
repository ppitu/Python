
def selectsort(L, left, right):
	for i in range(left, right):
		k = i
		for j in range(i + 1, right + 1):
			if L[j] < L[k]:
				k = j
		item = L[k]
		while k > i:
			L[k] = L[k - 1]
			k = k - 1
		L[i] = item

def insertsort(L, left, right):
	for i in range(left + 1, right + 1):
		item =	L[i]
		j = i
		while j > left and L[j - 1] > item:
			L[j] = L[j - 1]
			j = j - 1
		L[j] = item
	
def bubblesort(L, left, right):
	limit = right
	while True:
		k = left - 1
	for i in range(left, limit):
		if L[i] > L[i + 1]:
			swap(L, i, i + 1)
			k = 1
		if k > left:
			limit = k
		else:
			break

def shakersort(L, left, right):
	k = right
	while left < right:
		for j in range(right, left, -1):
			if L[j - 1] > L[j]:
				swap(L, j - 1, j)
				k = j
		left = k

		for j in range(left, right):
			if L[j] > L[j + 1]:
				swap(L, j, j + 1)
				k = j
		right = k

def shellsort(L, left, right):
	h = 1
	while h <= (right - left) // 9:
		h = 3*h + 1
	while h > 0:
		for i in range(left + h, right + 1):
			j = i
			item = L[i]
			while j >= left + h and item < L[j - h]:
				L[j] = L[j - h]
				j = j - h
			L[j] = item
		h = h// 3


def quicksort(L, left, right):
	if left >= right:
		return
	swap(L, left, (left + right) // 2)
	pivot = left
	for i in range(left + 1, right + 1):
		if L[i] < L[left]:
			pivot += 1
			swap(L, pivot, i)
	swap(L, left, pivot)
	quicksort(L, left, pivot - 1)
	quicksort(L, pivot + 1, right)

def mergesort(L, left, right):
	"""Sortowanie przez scalanie."""
	if left < right:
		middle = (left + right) // 2   # wyznaczanie środka 
		mergesort(L, left, middle)
		mergesort(L, middle + 1, right)
		merge(L, left, middle, right)   # scalanie
