with open("practice.txt1","r") as f:
    data = f.read()

new_data = data.replace("java","Python")
print(new_data) # print the new data.  

with open("practice.txt1","w") as f:
    f.write(new_data)   # overwrite the text file.