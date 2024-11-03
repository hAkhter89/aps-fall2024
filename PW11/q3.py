#############################################################################
# Note:                                                                     #
# 1. You may not use any helper functions. Please write your program using  #
#    only one recursive function.                                           #
# 2. You may not use loops or global variables. Please use a recursive      #
#    approach using local variables only.                                   #
#############################################################################

def devowelify(s):
    """
    Recursively removes vowels (a, e, i, o, u) from the string s.

    Parameters:
    s (str): The input string.

    Returns:
    str: The string with all vowels removed.
    """
    
    # WRITE YOUR CODE HERE
    if s == '':
        return ''
    else:
        if s[0] in 'aeiou' or s[0] in 'AEIOU':
            return '' + devowelify(s[1:])
        else: return s[0] + devowelify(s[1:])

#############################################################################
# Let's test your code on visible test cases... Run your code file and      #
# check manually whether the code is running as expected...                 #
#############################################################################

# If our code is indeed recusive, let's check the output is also as expected! :)
print(devowelify('Defenestrate'))
# Should print 'Dfnstrt'

print(devowelify('The quick brown fox jumps over the lazy dog.'))
# Should print 'Th qck brwn fx jmps vr th lzy dg.'

##################################################################
# YOU CAN DO FURTHER CUSTOM TESTING BELOW ....                   #
##################################################################




# Testing For all testcases 
# In order to test your function, type the following command on the terminal:
# pytest test_q3.py


