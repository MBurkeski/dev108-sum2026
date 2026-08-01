# This is where you will code your three functions 
# Be sure to write documentation for this module. 
# Refer to your book chapter for instructions on how to do this.

# Instructions
# Within your main python program file, write code that will ask the user to enter a first and last name input and then call your functions that you have defined in your nameformat module to output the three different versions of their name. 
# Only ask for the first and last name ONCE at the beginning of the program.
# There should be one input and then you will call these three different functions. 
# Create a menu system and give the users a choice of which output format they would like to see with a loop to give them options to keep choosing an option from the menu until they choose Exit.
# You should also have one option in the menu system - View Documentation - which will print out the module documentation that you have created in the nameformat.py file. 
# Refer to Chapter 4 on how to document your module. 
#       The first function sayHello() will take a first name and return a string that says Hello to the first name input followed by an exclamation point is. 
#       ex:  Hello Tony!
#       The second function fullName() will take a first and last name and return a string value with a first and last name concatenated with a space.  
#       ex: Tony Stark
#       The third function lastNameFirst() will take a first and last name and return a string value with a last name and first name, concatenated with a comma and a space. 
#       ex: Stark, Tony



# Name: Morgan Burke
# Date: 7/26/2026
# Lab Activity 6 - Modules, Documentation & Debugging



print()
# Title for assignment
print("The NameFormat module")
print()
print("Hello!")
print()

# get first and last name from user
first_name = (input("Please enter your first name: "))
last_name = (input("Please enter your last name: "))
print()
print("please review the menu options below to selection your choice of output format.")
print("** MENU **")
print()
print("1 - Say Hello\n2 - Output Full Name\n3 - Output Last Name, First Name\n4 - Read Documentation\n5 - Exit")

# say_hello() ex: Hello Tony!
def say_hello(first_name):
    """A simple function that takes the first_name input and says hello to that name"""
    print("Hello", first_name, "!")
    say_hello(first_name)
    print()

# fullName() ex: Tony Stark
def full_name(first_name, last_name):
    """A simple function that takes the first_name and last_name inputs and returns a string value with a first and last name concatenated with a space"""
    print(first_name + "" + last_name)
    print()

# lastNameFirst() ex: Stark, Tony
def last_name_first(last_name, first_name):
    """A simple function that takes the first_name and last_name inputs and returns a string value with the last name first and the first name last that is 
    concatenated with a space and a comma"""
    print(last_name + ", " + first_name)
    print()

# main function
# I left this main function section here because I wasn't sure if I needed to run all the functions in this one or only call them from the main one and I was afraid to delete it.
def main():
    while True:
        menu = int(input("\nWhat is your choice? "))
        if menu == 1:
            print("Hello " + first_name + "!")
            menu = int(menu)
        elif menu == 2:
            print(first_name, last_name)
        elif menu == 3:
            print(last_name + ", " + first_name)
        elif menu == 4:
            help(say_hello)
            help(full_name)
            help(last_name_first)
            continue
        elif menu == 5:
            print("Have a nice day! Goodbye")
            print()
            break
        else:
            print("Sorry, invalid entry. Please input values 1-5 only.")

# if started as the main module, call the main function
if __name__ == "__main__":
    main()

