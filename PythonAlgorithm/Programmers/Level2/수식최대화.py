import re
from itertools import permutations


def solution(expression):
    answer = 0
    op = re.sub('[0-9]', ' ', expression).split()
    ex = re.split('[^0-9]', expression)
    oper = list(permutations(set(op)))
    exp = []
    while ex:
        exp.append(ex.pop(0))
        if op:
            exp.append(op.pop(0))

    s = []
    for o in oper:
        _exp = exp[:]
        for x in o:
            while x in _exp:
                idx = _exp.index(x)
                _exp[idx - 1] = str(eval(_exp[idx - 1] + _exp[idx] + _exp[idx + 1]))
                _exp = _exp[:idx] + _exp[idx + 2:]
        s.append(_exp[-1])
    answer = max(abs(int(x)) for x in s)
    return answer