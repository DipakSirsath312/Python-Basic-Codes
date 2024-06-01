student = {
    "first name" : "dipak",
    "surname" : "sirsath",
    "address" : "mp,khetiya",
    "mobile" : "8305783244",
}

print(student.items())
print(list(student.items())) #type casting tuple to list.
pairs = list(student.items())
print(pairs[0])