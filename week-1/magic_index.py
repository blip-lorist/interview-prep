# Thanks to this blog post for helping me figure out what
# this question was asking. http://comproguide.blogspot.com/2014/02/finding-magic-index-of-array.html


def magic_index_recursive(input_array, start, end):
	# Find this midpt was really confusing. 
	# Originally, I was gonna divide the length of the array by two,
	# however, I realized that I'm passing the full input_array in 
	# for the recursion, rather than chopping this into left and
	# right side arrays.  

	mid = (start+ end) // 2

	# Base case: if input_array[mid] is equal to mid, that's the magic index
	if input_array[mid] == mid:
		print mid
	else: 
		# if the value at input_array[mid] is less than mid
		if input_array[mid] < mid:
			# disregard the left side
			# call recursive method on right side
			magic_index_recursive(input_array, mid+1, end)
		else:
			# disregard the right side
			# call recursive method on the left side
			magic_index_recursive(input_array, start, mid-1)


magic_index_on_right_side = [-1, 0, 1, 2, 4, 5]
magic_index_recursive(magic_index_on_right_side, 1, len(magic_index_on_right_side)-1)

magic_index_on_left_side = [-1, 1, 3, 4, 5]
magic_index_recursive(magic_index_on_left_side, 1, len(magic_index_on_left_side)-1)

just_magic_index = [0]
magic_index_recursive(just_magic_index, 0, len(just_magic_index)-1)
