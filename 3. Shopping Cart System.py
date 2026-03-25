#  Mini Project 3: Shopping Cart System
# Simulate an online cart. 


cart = []

def add_products():
    name = input("Enter Product Name:- ")
    price =float(input("Enter Prices:- "))
    qty = int(input("Enter Qauntity:- "))

    product = {
        "name" : name ,
        "price" : price ,
        "qyt" : qty
    }

    cart.append(product)
    print("Product Added")
add_products()


def display_card():
    if len(cart) == 0:
        print("Cart Empty")
    else:
        print("\n Cart Item")
        for i , item in enumerate(cart):
            print(i,item)
display_card()



def total_bill():
    total = 0
    for item in cart:
        total += item["price"] * item["qyt"]
    print("Total Bill:- ", total)
total_bill()


def remove_item():
    display_card()
    index = int(input("Enter Remove Index No:- "))

    if index < len(cart):
        print("Item Removed")
    else:
        print("Invalid Index")
remove_item()

# Menu

while True :
    print(" \n1.Add 2.Viwe 3.Total 4.Remove 5.Exit")
    choice = input("Enter Choice:- ")

    if choice == "1":
        add_products()
    elif choice == "2":
        display_card()
    elif choice == "3":
        total_bill()
    elif choice == "4":
        remove_item()
    elif choice == "5":
        break
    else:
        print("Invalid Choice")

