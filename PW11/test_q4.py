import pytest
import hashlib
import q4
from q4 import *

q4_testcases = [
    # Visible Testcases
    (-56, '-56', True),
    (0, '0', True),
    (3401, '3401', True),
    (-4534, '-4534', True),
    
    # Hidden Testcase
    (384, '37b73510175057c633ebe4beb0a34917fa2a0696432db43a4eeb2c3ff83a4c3b', False),
    (13478, 'f7f48475bdad14db54a8659a1a728ef48d1ae63fbaf3a5ffc44c1052e6f113d1', False),
    (-90340, 'ac9a1dbf985251628c17e3102b709a052bb5051cbc852407aad2a0d09a2203fb', False),
    (2180759, 'b853efc8e91d144832fa8ba0cef0185baa4663a1f43ce6ff09cbe3421e46ba19', False),
    (780978723, '535116f16bc07fcb49adf0f3030f7660d41d087c1a471eeadca73362ad47e4eb', False)
]

def hashcode(n: int) -> str:
    return hashlib.sha256(str(n).encode('utf-8')).hexdigest()

@pytest.mark.parametrize("s,result,testcase",q4_testcases)
def test_question4(s, result, testcase):
    import ast, inspect
    return_type = str
    # check that no helper functions are used.
    funcs = [obj for name, obj in inspect.getmembers(q4) if inspect.isfunction(obj)]
    if len(funcs) > 1:
        raise Exception('You may not use any helper functions. Please rewrite your program using only one recursive function.')
    # check that loops and globals are not used.
    taboo = (ast.Global, ast.For, ast.While)
    func  = funcs[0]
    source = inspect.getsource(func)
    nodes = ast.walk(ast.parse(inspect.getsource(func)))
    if any(isinstance(node, taboo) for node in nodes):
        raise Exception('You may not use loops or global variables. Please try a recursive approach using local variables only.')
    # check return type
    if 'str' in source:
        raise Exception('You may not convert to string directly. Please use the suggested method for the conversion.')    
    r = int_to_text(s)
    if isinstance(r, return_type):
        if testcase == True:
            assert int_to_text(s) == result
        else:
            assert hashcode(int_to_text(s)) == result
    else:
        raise Exception(f'Bad return type: {type(result)}. Please make sure to rerturn a {return_type}.')