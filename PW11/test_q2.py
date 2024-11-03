import pytest
import hashlib
import q2
from q2 import *

q2_testcases = [
    # Visible Testcases
    (2322, 654, 6, True),
    (12, 8, 4, True),
    (287, 175, 7, True),
    (175, 287, 7, True),
    (98, 56, 14, True),
    
    # Hidden Testcases
    (20, 28, '4b227777d4dd1fc61c6f884f48641d02b4d121d3fd328cb08b5531fcacdabf8a', False),
    (29, 233, '6b86b273ff34fce19d6b804eff5a3f5747ada4eaa22f1d49c01e52ddb7875b4b', False),
    (5031, 387, '25dac95b8f595046bc435139636b0e2f1ff6e0ea31a54f3c19e7e726fb98738b', False),
    (24, 36, '6b51d431df5d7f141cbececcf79edf3dd861c3b4069f0b11661a3eefacbba918', False),
    (87808, 151875, '6b86b273ff34fce19d6b804eff5a3f5747ada4eaa22f1d49c01e52ddb7875b4b', False),
    (10674846, 6174, '982cba6c0950686e37519d347bfa51deb9c933de7844a3800973b65d78c4667e', False)
]

def hashcode(n: int) -> str:
    return hashlib.sha256(str(n).encode('utf-8')).hexdigest()

@pytest.mark.parametrize("a,b,result,testcase",q2_testcases)
def test_question2(a, b, result, testcase):
    import ast, inspect
    return_type = int
    # check that no helper functions are used.
    funcs = [obj for name, obj in inspect.getmembers(q2) if inspect.isfunction(obj)]
    if len(funcs) > 1:
        raise Exception('You may not use any helper functions. Please rewrite your program using only one recursive function.')
    # check that loops and globals are not used.
    taboo = (ast.Global, ast.For, ast.While)
    func  = funcs[0]
    nodes = ast.walk(ast.parse(inspect.getsource(func)))
    if any(isinstance(node, taboo) for node in nodes):
        raise Exception('You may not use loops or global variables. Please try a recursive approach using local variables only.')
    # check return type
    r = gcd(a, b)
    if isinstance(r, return_type):
        if testcase == True:
            assert gcd(a, b) == result
        else:
            assert hashcode(gcd(a, b)) == result
    else:
        raise Exception(f'Bad return type: {type(result)}. Please make sure to rerturn a {return_type}.')