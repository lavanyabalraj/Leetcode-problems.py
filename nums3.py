nums1=[1,2,3,0,0,0]
m=3
n=3
nums2=[2,5,6]
result=[]
if m>0:
    for i in range(0,m):
        result.append(nums1[i])
if n>0:
    for j in range(0,n):
        result.append(nums2[j])
    for i in range(len(result)):
        nums1[i] = result[i]
nums1.sort()
print( nums1)