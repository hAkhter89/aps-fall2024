import pytest
import hashlib
from q7 import *

q7_testcases = [
    # Visible Testcases
    ('3[ac]', 'acacac', True),
    ('2[abc]3[cd]ef', 'abcabccdcdcdef', True),

    # Hidden Testcases
    ('3[a]2[bc]', 'bb313779800d8c637af5d73a750fdc547202af2af854c22148dabfae57196eb0', False),
    ('ab9[cd]2[ef]g', 'f94f07fd5f1fefdf8110ab5e4acc59339ec9dda2617b4e47869365e05cce14de', False),
    ('2[a]2[b]cd', '81696bf1bbbbbbb539357d661d3ed161534a7ad9d4ac81750629b11dbd1bc998', False)
]

def hashcode(n: int) -> str:
    return hashlib.sha256(str(n).encode('utf-8')).hexdigest()

@pytest.mark.parametrize("s,result,testcase",q7_testcases)
def test_question7(s, result, testcase):
    if testcase == True:
        assert decode(s) == result
    else:
        assert hashcode(decode(s)) == result