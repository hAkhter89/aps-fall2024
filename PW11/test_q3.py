import pytest
import hashlib
import q3
from q3 import *

q3_testcases = [
    # Visible Testcases
    ('Defenestrate', 'Dfnstrt', True),
    ('The quick brown fox jumps over the lazy dog.', 'Th qck brwn fx jmps vr th lzy dg.', True),
    
    # Hidden Testcases
    ('I owe you a ewe.', '44898cdb9d5ce6fe69e02a3c33714385d8b318c3ebc16810931cf3f77ab7aeb3', False),
    ('','e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855', False)]

def hashcode(n: int) -> str:
    return hashlib.sha256(str(n).encode('utf-8')).hexdigest()

@pytest.mark.parametrize("s,result,testcase",q3_testcases)
def test_question3(s, result, testcase):
    import ast, inspect
    return_type = str
    # check that no helper functions are used.
    funcs = [obj for name, obj in inspect.getmembers(q3) if inspect.isfunction(obj)]
    if len(funcs) > 1:
        raise Exception('You may not use any helper functions. Please rewrite your program using only one recursive function.')
    # check that loops and globals are not used.
    taboo = (ast.Global, ast.For, ast.While)
    func  = funcs[0]
    nodes = ast.walk(ast.parse(inspect.getsource(func)))
    if any(isinstance(node, taboo) for node in nodes):
        raise Exception('You may not use loops or global variables. Please try a recursive approach using local variables only.')
    # check return type
    r = devowelify(s)
    if isinstance(r, return_type):
        if testcase == True:
            assert devowelify(s) == result
        else:
            assert hashcode(devowelify(s)) == result
    else:
        raise Exception(f'Bad return type: {type(result)}. Please make sure to rerturn a {return_type}.')