# Calculate The Sum of Natural Numbers. 
def nal_sum(n):
    if(n == 0):
        return 0
    return nal_sum(n-1) + n

sum = nal_sum(5)
print(sum)