def difference_is_one_search(input_array, start_index, search_element):

    # Check  first element's value
    start_val = input_array[start_index]
    # Determine the difference between 8 and 3 (5 places)
    diff = abs(start_val - search_element)
   
    # Traverse the array with start_index + diff
    # Check array[traversal]. If match, then return traversal 
    traversal = start_index + diff
    if input_array[traversal] == search_element:
        print "%d first appears at index %d." % (search_element, traversal)
    else: # Recurse through array, starting at traversal
        start_index = traversal 
        difference_is_one_search(input_array, start_index, search_element)

# Example uses
input_array = [8, 7, 6, 7, 6, 5, 4, 3, 2, 3, 2, 3, 4, 3, 2, 1]
difference_is_one_search(input_array, 0, 3)

difference_is_one_search(input_array, 0, 7)
difference_is_one_search(input_array, 0, 2)
difference_is_one_search(input_array, 0, 1)

