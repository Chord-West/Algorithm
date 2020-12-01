
def solution(begin, target, words):
    answer = 0
    n = len(words)
    visited=[0]*n
    graph=[[] for _ in range(n)]

    for i,x in enumerate(words):        
        for j,y in enumerate(words):
            count=0
            for k in range(len(x)):
                if x[k]==y[k]:
                    count+=1
            if count>1:
                graph[i].append(j)
                
    start =[]   
    for i,x in enumerate(words):
       count=0
       for j in range(len(x)):
                if x[j]==begin[j]:
                    count+=1
       if count>1:
            start.append(i)

    for x in graph:
        x.sort()

    def dfs(start,count):
        visited[start]=count
        if words[start]==target:
            nonlocal answer
            answer=count
        for x in graph[start]:
            if visited[x]==0:
                dfs(x,count+1)
    for x in start:
        count=0
        dfs(x,count)
        answer-=1
 
    return answer



begin ="hit"
target="cog"
words=["hot","dot","dog","lot","log","cog"]

print(solution(begin, target, words))