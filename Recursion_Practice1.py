Broken = ["itachi","obito","pain","jiraya","naruto"]
def print_list(list,idx=0):
    if(idx == len(list)):
        return
    print(list[idx])
    print_list(list,idx+1)

print_list(Broken)