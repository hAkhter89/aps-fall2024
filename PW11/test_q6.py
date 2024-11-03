import pytest
import hashlib
import q6
from q6 import *

q6_testcases = [
    # Visible Testcases
    ('ADD', 7172, 71725, True),
    ('ADD', 92011, 920113, True),
    ('VERIFY', 313370, True, True),
    ('VERIFY', 678291, False, True),

    # Hidden Testcases
    ('ADD', 14, 'd6f0c71ef0c88e45e4b3a2118fcb83b0def392d759c901e9d755d0e879028727', False),
    ('ADD', 67890, '34f6ee350f892c89cfa2ae76f6dae8f34f423ab9fed893e01d8422aa54f7e25b', False),
    ('VERIFY', 172653, '3cbc87c7681f34db4617feaa2c8801931bc5e42d8d0f560e756dd4cd92885f18', False),
    ('VERIFY', 529197, '60a33e6cf5151f2d52eddae9685cfa270426aa89d8dbc7dfb854606f1d1a40fe', False)
]

def hashcode(n: int) -> str:
    return hashlib.sha256(str(n).encode('utf-8')).hexdigest()

@pytest.mark.parametrize("operation,idnum,result,testcase",q6_testcases)
def test_question6(operation, idnum, result, testcase):
    import ast, inspect, sys
    taboo = (ast.Global, ast.For, ast.While)
    funcs = [obj for name, obj in inspect.getmembers(q6)
         if inspect.isfunction(obj)]
    
    for func in funcs:
        nodes = ast.walk(ast.parse(inspect.getsource(func)))
        if any(isinstance(node, taboo) for node in nodes):
            raise Exception('You may not use global variable references, for loops, or while loops in your program. Please rewrite your program using recursion, local variables and parameters.')

    choice = operation
    if choice == 'ADD':
        if testcase == True:
            assert add_check_digit(idnum) == result
        else:
            assert hashcode(add_check_digit(idnum)) == result
    elif choice == 'VERIFY':
        if testcase == True:
            assert verify_check_digit(idnum) == result
        else:
            assert hashcode(verify_check_digit(idnum)) == result
