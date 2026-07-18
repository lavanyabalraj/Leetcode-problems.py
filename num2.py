digits=[1,2,3]
n=0
result=[]

for i in range(0,len(digits)):
    n=n*10+digits[i]
n=n+1
print(n)
while n>0:
    rem=n%10
    n=n//10
    result.append(rem)
result.reverse()
print(result)