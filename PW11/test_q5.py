import pytest
import hashlib
import q5
from q5 import *

q5_testcases = [
    # Visible Testcases
    (2, 3, 5, 6, 1091, True),
    (1, 2, 0, 10, 512, True),
    (1, 2, 1, 8, 255, True),
    (3, 4, 2, 4, 234, True),
    (9, 15, 7, 1, 9, True),

    # Hidden Testcases
    (2, 5, 0, 6, 'f8f3899a82eb30fee34728129408a0f570f7acee7b84d1abc297deb00fb36002', False),
    (1, 7, 1, 4, '26d228663f13a88592a12d16cf9587caab0388b262d6d9f126ed62f9333aca94', False),
    (2, 5, 3, 5, 'c0d2b0fe4d7671d1bb90703e6ab60ab14f01998648c45ba1da553283f8ab9dd6', False),
    (3, 4, 5, 6, '0f9305fb9daaca6e97608d3bdcf8961b59b080bdffe35613e1deade56823785f', False),
    (11, 23, 8, 1, '4fc82b26aecb47d2868c4efbe3581732a3e7cbcc6c2efb32062c08170a05eeb8', False)
]

def hashcode(n: int) -> str:
    return hashlib.sha256(str(n).encode('utf-8')).hexdigest()

@pytest.mark.parametrize("start,multiplier,bonus,level,result,testcase",q5_testcases)
def test_question5(start, multiplier, bonus, level, result, testcase):
    import ast, inspect
    taboo = (ast.Global, ast.For, ast.While)
    funcs = [obj for name, obj in inspect.getmembers(q5)
            if inspect.isfunction(obj)]
    if len(funcs) > 1:
        raise Exception('You may not use any helper functions. Please rewrite your program using only one recursive function.')
    for func in funcs:
        nodes = ast.walk(ast.parse(inspect.getsource(func)))
        if any(isinstance(node, taboo) for node in nodes):
            raise Exception('You may not use global variable references, for loops, or while loops in your program. Please rewrite your program using recursion, local variables and parameters.')
    if testcase == True:
        assert level_up(start, multiplier, bonus, level) == result
    else:
        assert hashcode(level_up(start, multiplier, bonus, level)) == result