def solution(p):
    if p == '':
        return p
    u, v = devide(p)
    reverse = {'(': ')', ')': '('}

    if validate(u):
        return u + solution(v)
    tmp = ''
    for x in u[1:-1]:
        tmp += reverse[x]

    return "(" + solution(v) + ")" + tmp


def devide(p):
    lb, rb = 0, 0
    for i, v in enumerate(p):
        if v == '(':
            lb += 1
        else:
            rb += 1
        if lb > 0 and lb == rb:
            return p[:i + 1], p[i + 1:]


def validate(w):
    stack = []
    for brace in w:
        if brace == '(':
            stack.append(brace)
        elif brace == ')':
            if stack and stack[-1] == '(':
                stack.pop()
            else:
                stack.append(brace)
    return True if len(stack) == 0 else False
