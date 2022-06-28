
nums = [1,2,3,4]
sum=1
out=[]
for i in range(0,len(nums)):
    out.append(sum)
    sum*=nums[i]
sum=1
for i in range(len(nums)-1,-1,-1):
    out[i] = out[i]*sum
    sum = sum*nums[i]

print(out)