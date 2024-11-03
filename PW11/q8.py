def empirical_formula(sym_x, sym_y, sym_z, mass_x, mass_y, mass_z, perc_x, perc_y, perc_z):
    """
    Calculates the empirical formula of a chemical compound from given data.

    Args:
        sym_x (str): Symbol of the first element.
        sym_y (str): Symbol of the second element.
        sym_z (str): Symbol of the third element.
        mass_x (float): Relative atomic mass of the first element.
        mass_y (float): Relative atomic mass of the second element.
        mass_z (float): Relative atomic mass of the third element.
        perc_x (float): Percentage composition of the first element.
        perc_y (float): Percentage composition of the second element.
        perc_z (float): Percentage composition of the third element.

    Returns:
        None: Prints the empirical formula or an error message.
    """

    # WRITE YOUR CODE HERE
    molarratio = [perc_x/mass_x, perc_y/mass_y, perc_z/mass_z] # X Y Z
    if molarratio[0] < molarratio[1] and molarratio[2]:
        unrounded = [molarratio[0]/molarratio[0], molarratio[1]/molarratio[0], molarratio[2]/molarratio[0]]
    elif molarratio[1] < molarratio[0] and molarratio[2]:
        unrounded = [molarratio[0]/molarratio[1], molarratio[1]/molarratio[1], molarratio[2]/molarratio[1]]
    elif molarratio[2] < molarratio[1] and molarratio[0]:
        unrounded = [molarratio[0]/molarratio[2], molarratio[1]/molarratio[2], molarratio[2]/molarratio[2]]
    # unrounded list in the order X Y Z
    for x in unrounded:
        if abs(x-round(x)) > 0.1:
            print('The empirical formula cannot be ascertained.')
            return
    print(f'{sym_x} {round(unrounded[0])} {sym_y} {round(unrounded[1])} {sym_z} {round(unrounded[2])}')

#############################################################################
# Let's test your code on visible test cases... Run your code file and      #
# check manually whether the code is running as expected...                 #
#############################################################################

empirical_formula('H', 'C', 'N', 1.01, 12.01, 14.01, 3.7, 44.44, 51.85)
# Should print 'H 1 C 1 N 1'

empirical_formula('H', 'C', 'O', 1.01, 12.01, 16.0, 6.71, 40.0, 53.29)
# Should print 'H 2 C 1 O 1'

empirical_formula('H', 'N', 'O', 1.01, 14.01, 16.0, 1.6, 22.23, 76.17)
# Should print 'H 1 N 1 O 3'

empirical_formula('H', 'S', 'O', 1.01, 32.07, 16.0, 2.06, 32.69, 65.25)
# Should print 'H 2 S 1 O 4'

empirical_formula('C', 'H', 'O', 12.01, 1.01, 16.0, 31.59, 5.3, 63.11)
# Should print 'The empirical formula cannot be ascertained.'

##################################################################
# YOU CAN DO FURTHER CUSTOM TESTING BELOW ....                   #
##################################################################




# Testing For all testcases 
# In order to test your function, type the following command on the terminal:
# pytest test_q8.py