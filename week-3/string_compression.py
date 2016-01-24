def string_compression_recursive(string, start):
    '''
    4. Implement a method to perform a basic string compression using the counts of repeated
    characters. For example, the string aabccccaaa would become a2b1c4a3. If the compressed string would not become smaller than the original string, your method should return the original string.
    '''
   
    # Base case: When compression length (uniques X 2) will be > string length
    # Base case: When start value is the end of the string
    if start >= len(string):
        return string
    else: 
        string = list(string)

        count = 0

        # Look at the start value
        current_letter = string[start]

        # Iterate
        for i in range(start, len(string)):
            # If dups are found, increment counter the number of times this value occurs
            if string[i] == current_letter and i == len(string) - 1:
               count += 1
               end = i + 1
               break
            elif string[i] == current_letter:
               count += 1
            else:
            # If unique or string end is found, record this as the end and stop 
                end = i 
                break

        # Remove dups, replace with current letter and count
        if count > 0:
            del string[start:end]
            string.insert(start, str(count))
            string.insert(start, current_letter) 

        string = ''.join(string)

        # Recurse with new start location
        return string_compression_recursive(string, start + 2)

def compression_wrapper(string):
    ''' 
    Checks the string once to see if there's any point for compression.
    If the original string length < unique letters * 2, then there is 
    no reason to compress the string.
    '''

    unique_count = len(set(string))
    if unique_count * 2 > len(string):
        print string

    else:
        print string_compression_recursive(string, 0)
 

# Examples
compression_wrapper('asdf')
compression_wrapper('aasdfff')
compression_wrapper('aasddfff')
compression_wrapper('aaaddfffff')
