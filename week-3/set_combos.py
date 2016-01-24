# input = ['a', 'b', 'c']
# output = ['', 'c', 'b', 'bc', 'a', 'ac', 'ab', 'abc']

def set_combo_recursive(array, start, output = ["_"]):

    if start < 0:
        print output
    else:
        combo_string = ""
        for element in output: # "_"
            import pdb; pdb.set_trace() 
            if element == "_":
                combo_string += array[start] # "c"
                output.append(combo_string)
            else: 
                combo = element + array[start] #  "c" + "b"
                combo_string + ", %s" % combo # append ", cb"
            
        output.append(combo_string)
        
        start -= 1

        set_combo_recursive(array, start, output)

input_array = ['a', 'b', 'c']
set_combo_recursive(input_array, 2)
