def check_world():
    world = "Learning"
    with open("practice.txt1","r") as f:
        data = f.read()
        if(data.find(world) != -1):
            print("Found")
        else:
            print("Not Found")

check_world()
