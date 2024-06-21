nums = (1,4,9,16,25,36,49,64,81,100)
x = int(input("Enter The Number:-"))
i = 0
while i < len(nums):
    if(nums[i] == x):
        print("Found at Index",i)
        break
    else:
        print("Finding...")
        i+=1