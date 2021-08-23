def solution(lines):
    answer = 0
    timeline=[]
    for line in lines:
        time,cost = line.split()[1:]
        h,m,s =time.split(':')
        s.replace('s','')
        end = (int(h)*3600+int(m)*60+float(s))*1000
        start = end - float(cost[:-1])*1000 + 1
        timeline.append((start,end))
    for x in timeline:
        answer = max(answer,find(timeline,x[0],x[0]+1000), find(timeline,x[1],x[1]+1000))

    return answer

def find(timeline,start,end):
    cnt = 0
    for x in timeline:
        if x[0]<end and x[1]>=start:
            cnt+=1
    return cnt