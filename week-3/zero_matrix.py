def zero_matrix(matrix):
    ''' 
    Write an algorithm such that if an element in an MxN matrix is 0, its entire row and column are set to 0.
    '''
    # Look at each row, check for zero values
    for row in matrix:
        for i, value in enumerate(row):
            # If there is a 0, then flip all values in row to zero
            if value == 0:
                last_element = len(row)
                for i in range(0,last_element):
                   row[i] = 0 
                break
    # Look at each col
    # If any value is 0, flip all col values to 0
    print matrix

# Example input
input = [[0,1,0,0],
         [1,1,1,1],
         [0,1,1,0]]

zero_matrix(input)
# Ideal output
# output = [[0000],
#           [0100],
#           [0000]]

