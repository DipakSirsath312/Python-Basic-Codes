Tuple = (1,4,9,16,25,36,49,64,81,100)
x = int(input("Enter The Number:-"))

idx=0
for Ele in Tuple:
    if(Ele == x):
        print("number found at idx",idx)
    idx+=1