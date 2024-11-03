#############################################################################
# Note:                                                                     #
# 1. You may not use any helper functions. Please write your program using  #
#    only one recursive function.                                           #
# 2. You may not use loops or global variables. Please use a recursive      #
#    approach using local variables only.                                   #
#############################################################################

def power(a, b):
    """
    Recursively calculates a raised to the power of b using multiplication.

    Parameters:
    a (int): The base.
    b (int): The exponent

    Returns:
    int or float: The value of a^b.
    """

    # WRITE YOUR CODE HERE
    if b == 0:
        return 1
    elif b > 0:
        return a * power(a, b-1)
    else: return 1/a * power(a, b+1)

#############################################################################
# Let's test your code on visible test cases... Run your code file and      #
# check manually whether the code is running as expected...                 #
#############################################################################

# If our code is indeed recusive, let's check the output is also as expected! :)
print(power(3, 4))  # Should print 81
print(power(0, 2))  # Should print 0
print(power(2, 0))  # Should print 1
print(power(-2, 1))  # Should print -2
print(power(-2, -1))  # Should print -0.5

##################################################################
# YOU CAN DO FURTHER CUSTOM TESTING BELOW ....                   #
##################################################################


# Testing For all testcases 
# In order to test your function, type the following command on the terminal:
# pytest test_q1.py





