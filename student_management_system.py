
import csv
FILENAME = "students.csv"
def add_student():
    roll_number = input("Enter roll number: ")
    name = input("Enter student name: ")
    marks = input("Enter marks: ")
    with open(FILENAME, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([roll_number, name, marks])
    print("Student added successfully!")
def search_student():
    roll_number = input("Enter roll number to search: ")
    with open(FILENAME, "r", newline="") as file:
        reader = csv.DictReader(file)
        for student in reader:
            if student["Roll Number"] == roll_number:
                print("Student found!")
                print("Roll Number:", student["Roll Number"])
                print("Name:", student["Name"])
                print("Marks:", student["Marks"])
                return
    print("Student not found!")
def delete_student():
    roll_number = input("Enter roll number to delete: ")
    students = []
    found = False
    with open(FILENAME, "r", newline="") as file:
        reader = csv.DictReader(file)
        for student in reader:
            if student["Roll Number"] == roll_number:
                found = True
            else:
                students.append(student)
    if found:
        with open(FILENAME, "w", newline="") as file:
            fieldnames = ["Roll Number", "Name", "Marks"]
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(students)
        print("Student deleted successfully!")
    else:
        print("Student not found!")
print("===== STUDENT MANAGEMENT SYSTEM =====")
while True:
    print("\n----- MENU -----")
    print("1. Add Student")
    print("2. Search Student")
    print("3. Delete Student")
    print("4. Exit")
    choice = input("Enter your choice: ")
    if choice == "1":
        add_student()
    elif choice == "2":
        search_student()
    elif choice == "3":
        delete_student()
    elif choice == "4":
        print("Thank you for using the Student Management System!")
        break
    else:
        print("Invalid choice!")
