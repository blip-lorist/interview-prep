def replace_spaces(string):
    '''
    3. Write a method to replace spaces in a string with "%20"
    Arguments:
        string - input string
    '''
    original_end = len(string) - 1
    spaces = 0

    # Count the number of spaces inside of a string
    for char in string:
        if char == " ":
            spaces += 1

    # For each space, add two more to the end of the string to create room to shove things over
    additional_spaces = (spaces * 2)
    new_end = original_end + additional_spaces 
    
    string += (additional_spaces * " ") 
    
    # Transform string into an array type
    string = list(string)

    # Starting backward from the end of the original string, iterate
    for i in range(original_end, 0, -1):
        if string[i] == " ":
            # Fill the last available spots with '%20'
            string[new_end] = "0"
            new_end -= 1
            string[new_end] = "2"
            new_end -= 1
            string[new_end] = "%"
            new_end -= 1
        else:
            # Move the value to the next available free spot
            string[new_end] = string[i]
            # Decrement the next free spot
            new_end -= 1

    # Transform back into string type
    string = "".join(string) 

    print string



string = "Tell"
replace_spaces(string)

string = "all the truth, but tell it slant"
replace_spaces(string) 
