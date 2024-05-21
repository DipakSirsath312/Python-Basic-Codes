#Nesting

age = int(input("Enter Your Age :-"))
if(age >= 19):
    if(age >= 70):
        print("Can Not Drive")
    else:
        print("Can Drive")
else:
    print("Can Not Drive")