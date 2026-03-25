# Mini Project 10: Number Utility Tool
# Work with numbers.

num =int(input("Enter a Number:- "))
print("\n Conversions:- ")
print("Binory:- ",bin(num))
print("octal:- ",oct(num))
print("Hex:- ",hex(num))

print("\n Formatting")
print("With Commas :- ",format(num, ","))
print("Scientific:- ","{:.2e}".format(num))