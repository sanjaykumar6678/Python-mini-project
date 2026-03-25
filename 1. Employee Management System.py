# Employee Management System
# 1. Add Employees
# --------------------

employees = []

def add_employee ():
    name = input("Enter Name:- ")
    age = int(input("Enter Age:- "))
    role = input("Enter Role:- ")
    salary =float(input("Enter Salary:- "))

    emp = {
        "name" : name,
        "age" : age,
        "role" : role,
        "salary" : salary
    }

    employees.append(emp)
    print(emp)
add_employee()


# 2. Display Employee:
#------------------------

def display_employees():
    if len(employees) == 0:
      print("No Employee Found")
    else:
        print("\n Employee List")
        for i,emp in enumerate(employees):
            print(i,emp)
display_employees()



# 3. Update Employee
# --------------------

def update_employee ():
    display_employees()
    index = int(input("Index to update:- "))
    if index <len(employees):
        employees[index]["Name"]= input("New Name:- ")
        employees[index]["Age"]=int(input("New age:- "))
        employees[index]["Role"]= input("New Role:- ")
        employees[index]["Salary"]= float(input("New Salary:- "))
        print("Update Successfully")
    else:
        print("Invalid Index")
update_employee()


# 4. delete employee
# --------------------

def delete_employee():
    display_employees ()
    Index = int(input("Enter Index to Delete:- "))

    if Index < len(employees):
        employees.pop(Index)
        print("Deleted Successfully")
    else:
        print("Invalid Index")
delete_employee()

# 5. Main menu
# -----------------

while True:
    print("\n======= Employee Management =======")
    print(" 1. Add Employee")
    print(" 2. Display Employees")
    print(" 3. Update Employee")
    print(" 4. Delete Employee")
    print(" 5. Exit")

    choice = input("Enter Choices:- ")

    if choice == "1":
        add_employee ()
    elif choice == "2":
        display_employees ()
    elif choice == "3":
        update_employee ()
    elif choice =="4":
        delete_employee ()
    elif choice == "5":
        print("Exiting....")
        break
    else :
        print("Invalid Choice")


