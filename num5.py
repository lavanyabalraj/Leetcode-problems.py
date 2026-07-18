nums=[1,7,3,6,5,6]
if len(nums) == 0:
    print(0)
j = 0
for i in range(1, len(nums)):
    if nums[i] != nums[j]:
        j += 1
        nums[j] = nums[i]
print(j + 1)
        