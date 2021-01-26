import sys
sys.stdin = open("input.txt","r")

def reverse(arr):
    if arr==arr[::-1]:
        return True
    else:
        return False

if __name__ == "__main__":
    board = [list(map(int,input().split())) for _ in range(7)]
    row=[]
    col=[]
    sum=0

    for i in range(7):
        for j in range(7):
            row.append(board[i][j])
            col.append(board[j][i])
        for k in range(3):
            if reverse(row[k:5+k]):
                sum+=1
            if reverse(col[k:5+k]):
                sum+=1
        row.clear()
        col.clear()

    print(sum)

