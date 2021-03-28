import sys
sys.stdin = open("input.txt","rt")

N = int(input())
arr_n = list(map(int,sys.stdin.readline().split()))
M = int(input())
arr_m = list(map(int,sys.stdin.readline().split()))

dic = dict()

for i in arr_n:
    try :
        dic[i] += 1
    except:
        dic[i] = 1

for i in arr_m:
    try:
        print(dic[i] , end = " ")
    except:
        print(0, end=" ")