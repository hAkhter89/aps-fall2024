import pytest
import hashlib
from q1 import *

q1_testcases = [
    # Visible Testcases
    (3, 4, 81, True),
    (0, 2, 0, True),
    (2, 0, 1, True),
    (-2, 1, -2, True),
    (-2, -1, -0.5, True),

    # Hidden Testcases
    (20, 6, '9497c569906da61cab24fe8493a43546bf3c9855d3773aa7419532c3a497b0b2', False),
    (2, 5, 'e29c9c180c6279b0b02abd6a1801c7c04082cf486ec027aa13515e4f3884bb6b', False),
    (-2, 5, '368d8db27f0b80020fcc663cae685bc8f57b9c184189c26c0999392e8f13f6fc', False),
    (2, -5, 'd452e554a937076c10180be078a1505314596920d7ef15fcbd46e5eb9ccab764', False),
    (-2, -5, 'c3c7c4cebb376177b590ba627b60b03d1b0853f6a96d6492d99848f500c4e7fe', False)
    ]

def hashcode(n: int) -> str:
    return hashlib.sha256(str(n).encode('utf-8')).hexdigest()

@pytest.mark.parametrize("a,b,result,testcase",q1_testcases)
def test_question1(a, b, result, testcase):
    import inspect
    source = inspect.getsource(power)
    if 'for' in source or 'while' in source:
        raise Exception("Try to solve the problem recursively!")
    elif testcase == True:
        assert power(a, b) == result
    else:
        assert hashcode(power(a, b)) == result