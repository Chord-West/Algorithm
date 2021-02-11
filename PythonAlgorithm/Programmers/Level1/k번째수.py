def solution(array, commands):
    answer = []
    for x in commands:
        tmp=array[x[0]-1:x[1]]
        tmp.sort()
        answer.append(tmp[x[2]-1])
    return answer