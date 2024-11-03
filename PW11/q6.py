#############################################################################
# Note:                                                                     #
# 1. You may not use any helper functions. Please write your program using  #
#    only one recursive function.                                           #
# 2. You may not use loops or global variables. Please use a recursive      #
#    approach using local variables only.                                   #
#############################################################################

def helper_calculate_digit(n):
    if n == 0:
        return 0
    else:
        return ((n % 10)**2 + helper_calculate_digit(n//10)) % 7

def add_check_digit(idnum):
    """
    Adds a check digit to a given HU ID number.

    Parameters:
    idnum (int): A non-negative integer representing the HU ID.

    Returns:
    int: The HU ID with the check digit appended.
    """
    
    # WRITE YOUR CODE HERE
    return (idnum*10) + helper_calculate_digit(idnum)
    
    
def verify_check_digit(idnum):
    """
    Verifies the check digit of a given HU ID number.

    Parameters:
    idnum (int): A non-negative integer representing the HU ID with check digit.

    Returns:
    bool: True if the check digit is valid, False otherwise.
    """

    # WRITE YOUR CODE HERE
    if  helper_calculate_digit(idnum//10) == idnum % 10:
        return True
    else: return False

#############################################################################
# Let's test your code on visible test cases... Run your code file and      #
# check manually whether the code is running as expected...                 #
#############################################################################

# If our code is indeed recusive, let's check the output is also as expected! :)
print(add_check_digit(7172))   # Should print 71725
print(add_check_digit(92011))  # Should print 920113
print(verify_check_digit(313370))   # Should print True
print(verify_check_digit(678291))  # Should print False

##################################################################
# YOU CAN DO FURTHER CUSTOM TESTING BELOW ....                   #
##################################################################




# Testing For all testcases 
# In order to test your function, type the following command on the terminal:
# pytest test_q6.py