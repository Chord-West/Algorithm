def solution(record):
    answer = []
    p = dict()
    for word in record:
        com = word.split()[0]
        id = word.split()[1]
        if com == 'Enter':
            p[id] = word.split()[2]
            answer.append([id,'님이 들어왔습니다.'])
        elif com == 'Change':
            p[id] = word.split()[2]
        else:
            answer.append([id,'님이 나갔습니다.'])
    result=[]
    for id,word in answer:
        result.append(p[id]+word)
    return result