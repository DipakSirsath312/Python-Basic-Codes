#nested dictionary...
student = {
    "name" : "Dipak Sirsath",
    "subjects" : {
        "software engineering" : 34,
        "data structure" : 34,
        "java programing" : 46,
        "web development2" : 37,
    }
}

print(student)
print(student["subjects"])
print(student["subjects"]["java programing"])