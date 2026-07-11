# this is the starting file for Lab Activity 2.2
# create your own starting code for the instructions provided 

# Name: Morgan Burke
# Date: 7/10/2026
# Exercise 2-3: Create a simple program

# display of a welcome message
print()
print("Welcome to the Area and Perimeter Program")
print("Please note, this program only calculates for rectangles or squares.")
print()
print()

# get user name 
firstName = input("Let's get started! What is your first name?  ")
print()
print(firstName, "please enter the measurements for the length and width of your rectangle or square.")
print("Please make sure both numbers are in same units.")
print("======================")

# get measurements from the user
length = int(input(firstName + " please enter the length (same units): "))
width = int(input(firstName + " please enter the width (same units): "))

# calculations
area = round(length * width)
perimeter = round(length + length + width + width)

# format and display results
print("======================")
print("Area = ",area)
print("Perimeter = ", perimeter)
print()
# thank you message
print("Thank you " + firstName + " for using this program!")
print()
