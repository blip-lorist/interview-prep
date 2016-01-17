def expression_eval(input_string):
    ''' Evaluate an expression given only single digits and only 2 operators * and +. '''
    stack = []
    multiply_temp = []

    for char in input_string:
        try: # Check if number
            num = int(char)
            # If things need to be multiplied
            if len(multiply_temp) == 2:
                product = multiply_temp[0] * num
                multiply_temp = []
                stack.append(product)
            else:
            # Append numbers to be summed
                stack.append(num)
        except ValueError:
            if char == "+":
                pass
            elif char == "*":
               first_digit = stack.pop()
               multiply_temp.append(first_digit)
               multiply_temp.append(char)

    print sum(stack)


# Examples
input_string = "2 + 3 * 5 + 5"
print input_string
expression_eval(input_string)

input_string = "2 + 3 * 5 + 5 + 6 * 2"
print input_string
expression_eval(input_string)

