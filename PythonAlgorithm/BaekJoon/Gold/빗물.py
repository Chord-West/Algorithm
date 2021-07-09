import sys
sys.stdin = open("input.txt","rt")
input = sys.stdin.readline

H,W = map(int,input().split())
height = list(map(int,input().split()))
volume=0

left, right = 0, W-1
left_max, right_max = height[left], height[right]

while left<right:
    if left_max<=right_max:
        left+=1
        left_max=max(left_max,height[left])
        volume+=left_max-height[left]
    else:
        right-=1
        right_max = max(right_max, height[right])
        volume += right_max - height[right]
print(volume)