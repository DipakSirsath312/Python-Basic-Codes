marks = [77,97,64,85,55]

def grade(marks):
    if marks >= 90:
        return "A"
    elif 80 <= marks < 90:
        return "B"
    elif 70 <= marks < 80:
        return "C"
    elif 60 <= marks < 70:
        return "D"
    else:
        return "F"

grades = map(grade,marks) 

print("Exam Scores:-",marks)
print("Grades:-",list(grades))