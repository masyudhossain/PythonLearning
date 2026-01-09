marks = {
    "Masyud": 100,
    "Minhaz": 96,
    "Rohan": 74,
    65:"Alamin"
}

# print(marks.items())
# print(marks.keys())
# print(marks.values())
marks.update({"Masyud": 99, "Renuka": 100})
print(marks)

print(marks.get("Rohan")) # Prints None
print(marks["Rohan"]) # Returns an error