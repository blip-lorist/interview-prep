def binary_search_recursive(input_array):
	''' Find the non-duplicate element in a sorted array.'''

	# Base case: when one element remains
	if len(input_array) == 1:
		unique = input_array[0]
		print unique
	# Base case: when three elements remain
	elif len(input_array) == 3:
		midpoint = 1 
		# if previous val and midpoint val match 
		if input_array[midpoint-1] == input_array[midpoint]:
			# unique is the next val
			unique = input_array[midpoint+1]
		else:
			# unique is the previous val
			unique = input_array[midpoint-1]
		print unique
	# Else when the array is longer 
	else:
		# find the midpoint index of array
		# round down to nearest int (the double slash is python floor division)
		midpoint = len(input_array)//2

		# if midpt is odd 
		if midpoint % 2 != 0:
			# if previous number is a match to midpt val
			# and the count of previous elements is odd
			previous_count = len(input_array[0:midpoint])
			if (input_array[midpoint-1] == input_array[midpoint]) and (previous_count % 2 != 0):
				# the first half is ok, so collect the latter half
				end = len(input_array)
				halved_array = input_array[midpoint:end]
			# else
			else:
				# the first half isn't ok, collect it
				halved_array = input_array[0:midpoint]
		else:
			# if midpoint is even
			end = len(input_array)
			latter_count = len(input_array[midpoint+1:end])
			if (input_array[midpoint+1] == input_array[midpoint]) and (latter_count % 2 != 0):
			# if next number is match
			# and count of latter elements is odd
				# the latter half is okay, collect first half
				halved_array = input_array[0:midpoint]
			else:
				# else collect the latter half
				end = len(input_array)
				halved_array = input_array[midpoint:end]

		binary_search_recursive(halved_array)


input_array = [1, 1, 3, 3, 4, 5, 5, 7, 7, 8, 8]
print input_array
binary_search_recursive(input_array)
print

input_array = [1, 1, 3, 3, 4, 4, 5, 6, 6]
print input_array
binary_search_recursive(input_array)
print

input_array = [1, 2, 2]
print input_array
binary_search_recursive(input_array)
print

input_array = [1, 1, 2]
print input_array
binary_search_recursive(input_array)
print

input_array = [1]
print input_array
binary_search_recursive(input_array)

