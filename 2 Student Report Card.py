# Mini Project 2: Student Report Car
# Create a report system. 


def calculate_grade (avg):
    if avg >= 90:
        return "A"
    elif avg >= 75:
        return "B"
    elif avg >= 50:
        return "C"
    else :
        return "Fail"
    

def students_report():
    name = input("Enter Students Name:- ")

    m1 = int(input("Enter Your Mark 1:- "))
    m2 = int(input("Enter Your Mark 2:- "))
    m3 = int(input("Enter Your Mark 3:- "))

    total = m1 + m2 + m3 
    avg = total / 3

    Grade = calculate_grade(avg)

    print("\n" + "="*30)
    print("     Students Report Card")
    print("="*30)

    print(f"name : {name}")
    print(f"Marks : {m1},{m2},{m3}")
    print(f"Total : {total}")
    print(f"Average : {avg:.2f}")
    print(f"Grade : {Grade}")
    print("="*30)
students_report()

