def check_line():
    world = "Programming"
    data = True
    line_no = 1
    with open("practice.txt1","r") as f:
        while data:
            data = f.readline()
            if(world in data):
                print(line_no)
                return
            line_no += 1
    return -1
           
print(check_line())