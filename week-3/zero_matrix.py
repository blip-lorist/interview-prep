import copy

def zero_matrix(matrix):
    ''' 
    Write an algorithm such that if an element in an MxN matrix is 0, its entire row and column are set to 0.
    '''

    # Copy the matrix
    matrix_copy = copy.deepcopy(matrix) 
    
    # --- ROWS ---
    # Look at each row, check for zero values
    for row in matrix:
        for i, value in enumerate(row):
            # If there is a 0, then flip all values in row to zero
            if value == 0:
                last_element = len(row)
                for i in range(0,last_element):
                   row[i] = 0 
                break

    # --- COLS ---
    col_check = []
    # Look at each col
    # If any value is 0, add its index position to a col_check list 
    for row in matrix_copy:
        for i, value in enumerate(row):
            if value == 0:
                col_position = i
                col_check.append(col_position)
        
        # For every col_check position that contains a 0, go through all rows,
        # zeroing out that column

        for position in col_check:
            for row in matrix:
                row[position] = 0


    print matrix 


# Example 
input = [[0,1,0,0],
         [1,1,1,1],
         [0,1,1,0]]

zero_matrix(input)
# Ideal output
# output = [[0000],
#           [0100],
#           [0000]]

