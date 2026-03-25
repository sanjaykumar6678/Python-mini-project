# Mini Project 6: String Formatter Tool
#  Build a formatting utility.

name = input("Enter Your Name:- ")
product = input("Enter Your Name:- ")

sentence = f"{name} bought a {product}"

print("\n Formatted Sentence:- ")
print(sentence)

print("\n Alignment Output:- ")
print("Left :", sentence.ljust(30, "_"))
print("Right :", sentence.rjust(30, "_"))
print("Center :", sentence.center(30, "_"))