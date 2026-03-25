# Mini Project 9: Course Enrollment System
#  Manage student enrollments.

# Course Enrollment System

students = {}

def add_student():
    name = input("Enter Student Name: ")
    courses = input("Enter Courses (comma separated): ").split(",")
    students[name] = courses
    print("Student Added")


def update_courses():
    name = input("Enter Student Name to update: ")
    if name in students:
        courses = input("Enter New Courses: ").split(",")
        students[name] = courses
        print("Courses Updated")
    else:
        print("Student Not Found")


def display_students():
    if len(students) == 0:
        print("No Students Found")
    else:
        print("\n Student Details:")
        for name, courses in students.items():
            print(name, "->", ", ".join(courses))


# Menu

while True:
    print("\n1.Add Student 2.Update Courses 3.Display 4.Exit")
    choice = input("Enter choice: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        update_courses()
    elif choice == "3":
        display_students()
    elif choice == "4":
        break
    else:
        print("Invalid Choice")