#############################################################################
# Note:                                                                     #
# 1. You may not use any helper functions. Please write your program using  #
#    only one recursive function.                                           #
# 2. You may not use loops or global variables. Please use a recursive      #
#    approach using local variables only.                                   #
#############################################################################

def gcd(a, b):
    """
    Computes the greatest common divisor (gcd) of two non-negative integers 
    a and b using recursion.

    Parameters:
    a (int): A non-negative integer.
    b (int): A non-negative integer.

    Returns:
    int: The gcd of a and b.
    """

    # WRITE YOUR CODE HERE
    if a == 0:
        return b
    elif b == 0:
        return a
    else:
        return gcd(b, a - (b * (a//b)))

#############################################################################
# Let's test your code on visible test cases... Run your code file and      #
# check manually whether the code is running as expected...                 #
#############################################################################

# If our code is indeed recusive, let's check the output is also as expected! :)
print(gcd(2322, 654))  # Should print 6
print(gcd(12, 8))      # Should print 4
print(gcd(287, 175))   # Should print 7
print(gcd(175, 287))   # Should print 7
print(gcd(98, 56))     # Should print 14    

##################################################################
# YOU CAN DO FURTHER CUSTOM TESTING BELOW ....                   #
##################################################################




# Testing For all testcases 
# In order to test your function, type the following command on the terminal:
# pytest test_q2.py

