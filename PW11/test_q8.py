import pytest
import hashlib
import q8
from q8 import *
from sys import stderr

def xstrip(s):
    lst = s.split('\n')
    for i in range(len(lst)):
        lst[i]=lst[i].rstrip()
    return "\n".join(lst)

q8_testcases = [
    # Visible Testcases
    ('H', 'C', 'N', 1.01, 12.01, 14.01, 3.7, 44.44, 51.85, 'H 1 C 1 N 1', True),
    ('H', 'C', 'O', 1.01, 12.01, 16.0, 6.71, 40.0, 53.29, 'H 2 C 1 O 1', True),
    ('H', 'N', 'O', 1.01, 14.01, 16.0, 1.6, 22.23, 76.17, 'H 1 N 1 O 3', True),
    ('H', 'S', 'O', 1.01, 32.07, 16.0, 2.06, 32.69, 65.25, 'H 2 S 1 O 4', True),
    ('C', 'H', 'O', 12.01, 1.01, 16.0, 31.59, 5.3, 63.11, 'The empirical formula cannot be ascertained.', True),

    # Hidden Testcases
    ('C', 'O', 'S', 12.01, 16.0, 32.07, 19.05, 25.4, 55.55, '01eae2ea0c6f607887b0211b4c01cdf236093231b24003d75b85419b6c4880d2', False),
    ('C', 'O', 'F', 12.01, 16.0, 19.0, 18.18, 24.24, 57.58, '23b5bbeb5f5ad88dbd38767203138c08c62bd836fa233f0f27a7b9542c3ac339', False),
    ('P', 'O', 'Cl', 30.97, 16.0, 35.45, 20.2, 10.43, 69.36, '594e03df3aab0c2efe7e3a99d32e25ede961a613f6928ecdb7d08b0a0b150627', False),
    ('H', 'P', 'O', 1.01, 30.97, 16.0, 3.08, 31.61, 65.31, '7dfa51b23e70262bf4c267107f10b12fe3580d3cc458d74a868ea8190131afa5', False),
    ('C', 'H', 'O', 12.01, 1.01, 16.0, 34.97, 2.93, 62.1, '1e60d3ed69c8c78a2d6a999573689489b4b36dba2421eff9e05e60a44a05ad91', False)
]

def hashcode(n: int) -> str:
    return hashlib.sha256(str(n).encode('utf-8')).hexdigest()

ignore_fn = {'test_question8'}

@pytest.mark.parametrize("sym_x, sym_y, sym_z, mass_x, mass_y, mass_z, perc_x, perc_y, perc_z,result,testcase",q8_testcases)
def test_question8(capsys, sym_x, sym_y, sym_z, mass_x, mass_y, mass_z, perc_x, perc_y, perc_z, result, testcase):
    import ast, inspect
    allow_globals = True
    allow_globals_msg = ''
    allowed_fn = {'empirical_formula': {'params': ['sym_x', 'sym_y', 'sym_z', 'mass_x', 'mass_y', 'mass_z', 'perc_x', 'perc_y', 'perc_z']}}
    required_fn = ['empirical_formula']
    required_fn_msg = 'Function is not defined.'
    restrict_fn = True
    restrict_fn_msg = 'You may only define functions as specified. Please read the requirements carefully.'
    restrict_params = True
    restrict_params_msg = 'Parameter names do not match. Please read the requirements carefully.'
    features = {ast.Import}
    taboo_features = True
    taboo_msg = 'You may not use external libraries. Please read the requirements carefully.'
    funcs = [(name, obj) for name, obj in inspect.getmembers(q8)
             if inspect.isfunction(obj)]
    fns = [name for name, obj in funcs]
    for fn in required_fn:
        if fn not in fns:
            raise Exception('For ' + fn + ':\n' + required_fn_msg)
    for fn, func in funcs:
        if fn in ignore_fn:
            continue
        if restrict_fn:
            if fn not in allowed_fn:
                raise Exception('For ' + fn + ':\n' + restrict_fn_msg)
        if restrict_params and fn in allowed_fn and 'params' in allowed_fn[fn]:
            params = list(inspect.signature(func).parameters)
            if params != allowed_fn[fn]['params']:
                raise Exception('For ' + fn + ':\n' + restrict_params_msg)
        if not allow_globals:
            closure = inspect.getclosurevars(func)
            closure_globals = set(closure.globals)
            for f in fns:
                if f in closure_globals:
                    closure_globals.remove(f)
            if closure_globals:
                raise Exception('For ' + fn + ':\n' + allow_globals_msg)
        if taboo_features:
            nodes = ast.walk(ast.parse(inspect.getsource(func)))
            if any(isinstance(node, tuple(features)) for node in nodes):
                raise Exception('For ' + fn + ':\n' + taboo_msg)

    if testcase == True:
        empirical_formula(sym_x, sym_y, sym_z, mass_x, mass_y, mass_z, perc_x, perc_y, perc_z)
        captured,err = capsys.readouterr()
        captured=captured[:-1]
        assert xstrip(captured) == xstrip(result)
    else:
        empirical_formula(sym_x, sym_y, sym_z, mass_x, mass_y, mass_z, perc_x, perc_y, perc_z)
        captured,err = capsys.readouterr()
        captured=captured[:-1]
        assert hashcode(xstrip(captured)) == xstrip(result)