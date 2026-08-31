
import json
print("===== JSON FILE READER =====")
filename = "students.json"
with open(filename, "r") as file:
    data = json.load(file)
print("\nStudent Details:")
for student in data["students"]:
    print("--------------------")
    print("Roll Number:", student["roll_number"])
    print("Name:", student["name"])
    print("Marks:", student["marks"])
