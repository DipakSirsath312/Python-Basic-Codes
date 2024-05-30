dict = {
    "key" : "value",
    "subjects" : ["python","java","c++","rust","go"],
    "topics" : ("dictionary","set"), 
    "name" : "Dipak",
    "grade" : "B+",
    "marks" : [75,65,87,76]
}

print(dict["name"])
print(dict["subjects"])
print(dict["topics"])

dict["name"] = "Alpesh" #overwrite
dict["surname"] = "sirsath" #Add New Key And value Pairs
print(dict)