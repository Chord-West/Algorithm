import sys


def main():
    # sys.stdin = open("sample_input.txt", "rt")
    input = sys.stdin.readline
    T = int(input())
    for t in range(1, T + 1):
        a, b, l = input().split()
        L = int(l)
        fil = input().rstrip('\n')
        A = [0 for i in range(6 - len(a))]
        for x in a:
            A.append(int(x))
        B = [0 for i in range(6 - len(b))]
        for y in b:
            B.append(int(y))
        answer = 0
        oper = []
        for l in fil:
            if l == '+':
                oper.append(1)
            elif l == '-':
                oper.append(-1)
            else:
                oper.append(0)
        oper2=oper[::-1]
        ch=False
        for i in range(6 - L + 1):
            tmp = A[:]
            tmp2 = A[:]
            cnt=0
            while A[i] != B[i] and cnt<11:
                for j in range(len(oper)):
                    tmp[i + j] += oper[j]
                    if tmp[i + j] < 0 or tmp[i + j] > 9:
                        break
                for k in range(len(oper2)):
                    tmp2[i + k] += oper2[k]
                    if tmp2[i + k] < 0 or tmp2[i + k] > 9:
                        break
                answer += 1
                cnt+=1
                if tmp[i] == B[i]:
                    A = tmp
                elif tmp2[i] == B[i]:
                    A = tmp2
            if cnt==11:
                ch=True
        tmp = A[:]
        tmp2 = A[:]
        cnt = 0
        while A[-1]!=B[-1] and cnt<11:
            for j in range(len(oper)):
                tmp[-j] += oper[-j]
                if tmp[-j] < 0 or tmp[-j] > 9:
                    break
            for k in range(len(oper2)):
                tmp2[-k] += oper2[-k]
                if tmp2[-k] < 0 or tmp2[-k] > 9:
                    break
            answer += 1
            cnt += 1
            if tmp[-1] == B[-1]:
                A = tmp
            elif tmp2[-1] == B[-1]:
                A = tmp2

        if cnt == 11:
            ch = True
        if ch:
            print("#{} {}".format(t, -1))
        else:
            print("#{} {}".format(t, answer))


main()