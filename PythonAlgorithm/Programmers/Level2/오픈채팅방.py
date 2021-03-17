def solution(record):
    answer = []
    a={x.split()[1]:x.split()[2] for x in record if len(x.split())==3}
    for x in record:
        y=x.split()
        if y[0]=='Enter':
            answer.append('{}님이 들어왔습니다.'.format(a[y[1]]))
        elif y[0]=='Leave':
            answer.append('{}님이 나갔습니다.'.format(a[y[1]]))
    return answer