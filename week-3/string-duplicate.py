def is_unique(string):
    ''' 
    Implement an algorithm to determine if a string has all unique characters. What if you cannot use additional data structures?
    Return True if string is unique, False if not
    '''

    # Normally, I would want to use a hash dictionary to check if something is a duplicate. 
    # However, since I can't use additional data structures, then I will sort the string and
    # check elements in pairs until I find a match.

    sorted_str = ''.join(sorted(string)) 
   
    for i, letter in enumerate(sorted_str):
        try:
            if letter == sorted_str[i+1]:
               return False
        except: 
            pass

    return True


string = "asdf"
print is_unique(string)

string = "indifferent"
print is_unique(string)
