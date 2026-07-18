nums=[2,3,4,4,8]
nums.sort()
smallest=nums[0]
greatest=nums[len(nums)-1]
for i in range(2,greatest):
    if smallest!=greatest:
        if smallest%i==0  and greatest%i==0:
            ans=i
            break
    else:
            ans=smallest
            break
else:
    ans=1
print(ans)