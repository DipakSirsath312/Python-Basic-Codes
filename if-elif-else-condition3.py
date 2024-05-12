A = int(input("Enter Number:-"))
G = input("m/f:-")
if(A ==  1 or A == 2 and G == "m"):
    print("Fee is 100")
elif(A == 3 or A == 4 or G == "f"):
    print("Fee is 200")
elif(A == 5 or G == "m"):
    print("300")
else:
    print("No Fee")