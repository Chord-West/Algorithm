def solution(brown, yellow):
    _sum = brown+yellow
    arr = []
    idx = _sum
    while idx>0:
        if _sum%idx ==0:
            arr.append(idx)
        idx-=1
    cnt = len(arr)
    arr2=[]
    for i in range(cnt//2+1):
        if arr[cnt-1-i]>2:
            if brown+yellow - (arr[i]+arr[cnt-1-i]-2)*2 == yellow:
                return  [arr[i],arr[cnt-1-i]]
