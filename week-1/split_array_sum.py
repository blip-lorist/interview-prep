def split_array_sum(input_array):
    ''' Given a sorted array of n integers that has been rotated an unknown number of times, write code to find an element in the array. You may assume that the array was originally sorted in increasing order.
    
    Note: This doesn't account for arrays with negative numbers. :\
    ''' 
    # Sort the array
    sorted = input_array.sort()
    # Take the largest number
    largest_num = input_array.pop()
    # See if the sum of the other integers == largest number 
    if sum(input_array) == largest_num:
    # If so, return both arrays
        print input_array
        print largest_num
        print
    else:
        print "No sum include in array."
        print
input_array = [4, 1, 2, 12, 5]
split_array_sum(input_array)

input_array = [4, 1, 2, 11, 5]
split_array_sum(input_array)

input_array = [3, 21, 9, 2, 7]
split_array_sum(input_array)


