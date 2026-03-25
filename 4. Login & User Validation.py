# Mini Project 4: Login & User Validation
#  Basic authentication system.


users = {
    "Admin": "1234",
    "user" : "abcd"
}

def login ():
    username = input("Enter User Name:- ")
    password = input("Enter Password:- ")

    if username in users and users[username] == password :
        print("Login Successful")
    else:
        print("Invalid Password")
login()
