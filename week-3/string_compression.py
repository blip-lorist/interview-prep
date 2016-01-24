def string_compression_recursive(string, start):
    '''
    4. Implement a method to perform a basic string compression using the counts of repeated
    characters. For example, the string aabccccaaa would become a2b1c4a3. If the compressed string would not become smaller than the original string, your method should return the original string.
    '''


    # Base case: When start value is the end of the string
    if start == len(string) - 1:
        string = ''.join(string) 
        print string
    else: 
        string = list(string)

        count = 0

        # Look at the start value
        current_letter = string[start]

        # Iterate
        for i in range(start, len(string)):
            # If dups are found, increment counter the number of times this value occurs
            if string[i] == current_letter:
               count += 1
            else:
            # If unique is found, record this as the new start place and stop
                end = i 
                break

        
        # Remove dups, replace with current letter and count
        if count > 0:
            del string[start:end]
            string.insert(start, str(count))
            string.insert(start, current_letter) 

        # Recurse with new start location
        string_compression_recursive(string, start + 2)

string_compression_recursive("asdf", 0)
