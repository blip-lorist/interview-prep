def is_permutation(string_1, string_2):
    '''
    2. Given two strings, write a method to decide if one is a permutation
    of the other
    '''
    
    # I basically want to check if both of these words use the 
    # same letters. Seems like a hash lookup would be good. 
        

    # Base case: If the lengths differ, then they are not permutations
    if len(string_1) != len(string_2):
        return False

    letter_lookup = {}

    # Create our lookup dictionary
    for letter in string_1:
        letter_lookup[letter] = 1

    # Check to see if letters in string_2 have been logged
    for letter in string_2:
        # If a key cannot be found, immediately return false

        try: 
            letter_lookup[letter]
        except KeyError:
            return False
    
    # If the check is completed, return True
    return True


# Examples
# Feed it some anagrams!
print is_permutation('cruel', 'lucre')

# Feed it nonanagrams!
print is_permutation('kind', 'donation')
