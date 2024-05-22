#Find The Largest Number
a = int(input("Enter First Number:-"))
b = int(input("Enter Second Number:-"))
c = int(input("Enter Third Number:-"))
d = int(input("Enter four Number"))
if(a >= b and a >= c):
    print("first number is largest",a)
elif(b >= c and b >= d):
    print("second number is largest",b)
elif(c >= d):
    print("third number is largest",c)
else:
    print("fourth number largest",d)