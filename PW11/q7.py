def decode(cipher):
    """
    Decodes an encoded string of the format k[string].

    Repeats 'string' k times for each occurrence of the pattern.

    Args:
        cipher (str): The encoded string.

    Returns:
        str: The decoded message.
    """

    # WRITE YOUR CODE HERE
    flist = []
    while True:
        if cipher[0].isdigit() == False:
            flist.append(cipher[0])
            cipher = cipher[1:]
        else:
            break
    
    a = (cipher.split(']'))
    for x in a:
        x = str(x)
        if x != '':
            if x[0].isdigit() is True and x[1].isdigit() == True:
                flist.append((x[3:] * int(x[0]+x[1])))
            elif x[0].isdigit() is True:
                flist.append((x[2:] * int(x[0])))
            else:
                flist.append(x)
    return ''.join(str(x) for x in flist)

#############################################################################
# Let's test your code on visible test cases... Run your code file and      #
# check manually whether the code is running as expected...                 #
#############################################################################

print(decode('3[ac]'))   # Should print 'acacac'
print(decode('2[abc]3[cd]ef'))  # Should print 'abcabccdcdcdef'

##################################################################
# YOU CAN DO FURTHER CUSTOM TESTING BELOW ....                   #
##################################################################
print(decode('49[abc]ef'))




# Testing For all testcases 
# In order to test your function, type the following command on the terminal:
# pytest test_q7.py