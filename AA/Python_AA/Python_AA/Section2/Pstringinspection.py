import sys
#sys.stdin = open("input.txt","rt")

n = int(input())
for i in range(n):
    str=input()
    str=str.upper() # 대문자화시킴
    if str == str[::-1]:
        print("#{} YES".format(i+1))
    else:
        print("#{} NO".format(i+1))