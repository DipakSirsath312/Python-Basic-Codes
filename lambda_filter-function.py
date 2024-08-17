marks = [77,97,55,64,85,35]

def failing(score):
    return score < 60
 
result = filter(failing,marks)
print("Failing Scores:-",list(result))