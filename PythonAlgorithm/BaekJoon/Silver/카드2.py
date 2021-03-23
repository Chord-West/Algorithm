from collections import deque

arr=[x for x in range(1,int(input())+1)]
q=deque(arr)
while len(q)>1:
    q.popleft()
    q.append(q.popleft())
print(q.popleft())