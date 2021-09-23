# tuple = collection which is ordered and unchangeable used to group together related data

student = ("Jeb",21,"male")

print(student.count("Jeb"))
print(student.index("male"))

for x in student:
    print(x)

if "Jeb" in student:
    print("Jeb is here!")