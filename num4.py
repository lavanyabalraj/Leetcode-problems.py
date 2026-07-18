nums=[1,7,3,6,5,6]
sums2=0
sums1=0
for i in range(0,len(nums)):
    sums2=0
            
    for j in range(i+1,len(nums)):
        sums2=sums2+nums[j]
    if sums1==sums2:
        print( i)
    sums1=sums1+nums[i]
else:
  print(-1)