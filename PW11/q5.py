#############################################################################
# Note:                                                                     #
# 1. You may not use any helper functions. Please write your program using  #
#    only one recursive function.                                           #
# 2. You may not use loops or global variables. Please use a recursive      #
#    approach using local variables only.                                   #
#############################################################################

def level_up(start, multiplier, bonus, level):
    """
    Recursively calculates the number of chickens required to reach the specified level.

    Parameters:
    start (int): Initial number of chickens (non-negative).
    multiplier (int): Multiplier for chickens (positive).
    bonus (int): Bonus chickens added (non-negative).
    level (int): Target level (positive).

    Returns:
    int: Number of chickens needed at the specified level.
    """

    # WRITE YOUR CODE HERE
    if level == 1:
        return start
    else:
        return level_up((start * multiplier + bonus), multiplier, bonus, level - 1)

#############################################################################
# Let's test your code on visible test cases... Run your code file and      #
# check manually whether the code is running as expected...                 #
#############################################################################

# If our code is indeed recusive, let's check the output is also as expected! :)
print(level_up(2, 3, 5, 6))   # Should print 1091
print(level_up(1, 2, 0, 10))  # Should print 512
print(level_up(1, 2, 1, 8))   # Should print 255
print(level_up(3, 4, 2, 4))   # Should print 234
print(level_up(9, 15, 7, 1))  # Should print 9

##################################################################
# YOU CAN DO FURTHER CUSTOM TESTING BELOW ....                   #
##################################################################




# Testing For all testcases 
# In order to test your function, type the following command on the terminal:
# pytest test_q5.py