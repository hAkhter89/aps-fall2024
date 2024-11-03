#############################################################################
# Note:                                                                     #
# 1. You may not use any helper functions. Please write your program using  #
#    only one recursive function.                                           #
# 2. You may not use loops or global variables. Please use a recursive      #
#    approach using local variables only.                                   #
#############################################################################

def int_to_text(n):
    """
    Recursively converts an integer n to its s-t-r-i-n-g representation.

    Parameters:
    n (int): The integer to convert.

    Returns:
    s-t-r: The s-t-r-i-n-g representation of the integer.
    """

    # WRITE YOUR CODE HERE
    if n < 0:
        return '-' + int_to_text(-n)
    elif n < 10:
        return chr(n+48)
    else:
        return int_to_text(n//10) + chr((n%10)+48)
        

#############################################################################
# Let's test your code on visible test cases... Run your code file and      #
# check manually whether the code is running as expected...                 #
#############################################################################

# If our code is indeed recusive, let's check the output is also as expected! :)
print(int_to_text(-56))   # Should print '-56'
print(int_to_text(0))   # Should print '0'
print(int_to_text(3401))   # Should print '3401'
print(int_to_text(-4534))   # Should print '-4534'

##################################################################
# YOU CAN DO FURTHER CUSTOM TESTING BELOW ....                   #
##################################################################




# Testing For all testcases 
# In order to test your function, type the following command on the terminal:
# pytest test_q4.py







