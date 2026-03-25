# Mini Project 5: Unique Visitor Counter
# Track unique visitors.

visitors = set()

def add_visitor():
    name = input("Enter Name:- ")
    visitors.add (name)
    print("Visitors Added")
add_visitor()

def show_visitor():
    print("\n Unique Visitors")
    for v in visitors:
        print(v)
    print("Total Unique Visitors:- ",len(visitors))
show_visitor()


# Menu
while True:
    print("\n1. add_visitor 2.show visitor 3. Exit")
    choice = input("Enter Choice")

    if choice == "1" :
        add_visitor()
    elif choice == "2":
        show_visitor()
    elif choice == "3":
        break
    else:
        print("Invalid Choice")
