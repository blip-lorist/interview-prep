def extra_paren(input_string):

    position_stack = []

    # Move through each character in string
    for i, char in enumerate(input_string):
        # If the char is an opening paren, toss its index into a stack
        if char == "(":
            position_stack.append(i)
        elif char == ")": # If it is a closing paren
            if len(position_stack) != 0:
                # Remove the last element (its corresponding opening paren) 
                position_stack.pop()
            else: # However, if this closing paren is the extra 
                # Add it to the stack
                position_stack.append(i)

    print "The extra paren is located at %d" % position_stack[0]

input_string = "(a+(b+c+d)"
extra_paren(input_string)

input_string = "(a+(b+c+d)))"
extra_paren(input_string)
