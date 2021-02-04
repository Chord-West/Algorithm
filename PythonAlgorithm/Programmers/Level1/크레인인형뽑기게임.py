def solution(board, moves):
    answer = 0
    n = len(board)
    dolls=[]
    stack=[0]
    for i in range(n):
        tmp=[]
        for j in range(n):
            if board[j][i]>0:
                tmp.append(board[j][i])
        dolls.append(tmp)
    dolls.insert(0,[0])
    for x in moves:
        if len(dolls[x])>0:
            d = dolls[x].pop(0)
            if d == stack[len(stack)-1]:
                stack.pop()
                answer+=2
            else:
                stack.append(d)
    return answer