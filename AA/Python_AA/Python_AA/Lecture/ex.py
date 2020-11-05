def solution(arr):
    d=[[[0 for x in range(2)] for y in range(len(arr))] for z in range(len(arr))]
    oper=[]

    for i in range(len(arr)):
        if arr[i]=="+":
            oper.append(1001)
        elif arr[i]=="-":
            oper.append(1002)
        else:
            oper.append(int(arr[i]))
            d[i][i][0]=oper[i]
            d[i][i][1]=oper[i]

    for i in range(2,len(arr),2):
        for j in range(0,len(arr)-i,2):
                dmax=0
                dmin=0
                max_n=-9999999
                min_n=9999999
                for k in range(j+1,i+j,2):  
                    if oper[k]==1001:
                        dmax= d[j][k-1][0] + d[k+1][i+j][0]
                        dmin = d[j][k-1][1] + d[k+1][i+j][1]
                        if(dmax>max_n):
                            max_n=dmax
                        if(dmin<min_n):
                            min_n=dmin
                    elif oper[k]==1002:
                        dmax= d[j][k-1][0] - d[k+1][i+j][1]
                        dmin = d[j][k-1][1] - d[k+1][i+j][0]
                        if(dmax>max_n):
                            max_n=dmax
                        if(dmin<min_n):
                            min_n=dmin

                d[j][i+j][0]= max_n
                d[j][i+j][1]= min_n
    return d[0][len(arr)-1][0]    




arr=	["1", "-", "3", "+", "5", "-", "8"]
print(solution(arr))