#Calculate Simple Interest

a = float(input("A:-"))                       
c  = float(input("C:-"))
b = float(input("B:-"))       
print(a*b*c/100)

 #Improved Codes -> 
 # principal  p
 # rate       r         si = p * r * t
 # Time       t               100

p = float(input("P:-"))
r = float(input("R:-"))
t = float(input("T:-"))
si = (p*r*t)/100
print(si)