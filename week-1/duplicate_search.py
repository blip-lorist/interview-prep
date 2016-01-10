def duplicate_search_recursive(input_array):
	''' Find the one duplicate in an array containing values 1 through n-1.
	Question 4: Given an array that contains numbers from 1 to n-1 and exactly 1 duplicate, find that duplicate.	
	'''
	# input_array = [3, 1, 4, 1, 2]  
	print "The input array is: ", input_array
	# Get the last element's value (2) 
	print "The value of the last element: ", input_array[len(input_array)-1]
	# Find where it's supposed to be input_array at the index of the last element's value (1)
	# Store that value in temp
	temp = input_array[input_array[len(input_array)-1]- 1]
	print "The value of temp:", temp
	# Base case: When the last element is equal to temp (before swap)
	if temp == input_array[len(input_array)-1]:
		print "The duplicate value is %d. \n" % temp
	else: 
		# Swap their places by making input_array[last_value - 1] = input_array[n-1] (value 2), then input_array[n-1] = temp (value 1)
		input_array[input_array[len(input_array)-1] - 1] = input_array[len(input_array)-1]
		input_array[len(input_array)-1] = temp

		duplicate_search_recursive(input_array)

input_array = [3, 1, 4, 1, 2]
duplicate_search_recursive(input_array)

input_array = [4, 4, 2, 3, 1]
duplicate_search_recursive(input_array)

input_array = [2, 4, 2, 1, 3]
duplicate_search_recursive(input_array)
