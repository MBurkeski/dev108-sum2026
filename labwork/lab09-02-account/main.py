# Starting file for Exercise 10-1

# Name: Morgan Burke
# Practice Lab 9, Exercise 10-1: Enhance the Create Account program
# 8/15/2026

# Instructions: 
# Review the code and run the program so that you understand the starting point. 
# Create and use a function to get a valid email address. 
# To be valid, the address has to contain an @ sign and end with ".com" 
# I do realize that email addresses can end in something other than .com, let's just pretend here for this exercise that .com is the only one. :) 
# Create and use a function to get a valid phone number. 
# To do that, remove all spaces, dashes, parentheses, and periods from the number. 
# Then, check to make sure that the phone number consists of 10 characters that are digits. 
# When all of the entries are valid, display a message similar to the one in the example
# including the phone number format that uses dots to group the digits. 
# You have creative license for the display/text and validation messages in this program. 
# As long as you are using functions calling them to validate your email and phone number, and outputting the formatted phone number, we are good! 
# Ensure that you have a title/greeting in your output. 
# e sure to have an exit message too. 
# Test and debug the program to make sure it works. 
# Be sure to comment your code to explain the process. 
# X Include your name, date, class and assignment name in the comments at the top of the program. 

# program title
def title():
    print()
    print("Welcome to the Account Validaton Program!")
    print("Please follow the prompts below to validate your account.")
    print()
    print("-" * 100)
    print("Account Validation Program ")
    print("-" * 100)   
    
# function to get the full name from the user    
def get_full_name():
    while True:
        name = input("Enter full name:              ").strip()  # eliminates a space at the beginning or end of the name
        if " " in name:
            return name
        else:
            print("You must enter your full name.")

# function to grab the first name from the input to pull the first name for the ouput message at the end    
def get_first_name(full_name):
    index1 = full_name.find(" ")
    first_name = full_name[:index1]
    return first_name

# function to get the password    
def get_password():
    while True:
        digit = False
        cap_letter = False
        password = input("Enter password:               ").strip()
        for char in password:
            if char.isdigit():
                digit = True
            elif char.isupper():
                cap_letter = True
        if digit == False or cap_letter == False or len(password) < 8:
            print(f"Password must be 8 characters or more \n"
                  f"with at least one digit and one uppercase letter.")
        else:
            return password

# function to get the email
def get_email():
    while True:
        email = input("Enter your email address:     ").strip()
        # get the index of the @ character
        # returns -1 if not found, returns index if found
        find_at = email.find("@")
        find_dot = email.find(".com", find_at)
        if find_at == -1 or find_dot == -1:
            print("Please enter a valid email address.")
        else:
            return email

# function to get the phone number
def get_phone_number():
    while True:
        phone = input("Enter phone number:           ").strip()
        for char in " -().":
            phone = phone.replace(char, "")
            if len(phone) != 10 or phone.isdigit() == False:
                print("Please enter a 10-digit phone number.")
            else:
                phone = (phone[0:3] + "." + phone[3:6] + "." + phone[6:])
                return phone

# main function
def main():
    title()
    print()
    full_name = get_full_name()  
    password = get_password()
    email = get_email()
    phone = get_phone_number()

    first_name = get_first_name(full_name)
    print()
    print(f"Hi {first_name}, thanks for creating an account.")    
    print()
    print("We'll text your confirmation code to this number: " + phone) 
    print("We'll also email your confirmation code as a back up to your email: " + email)    
    print("Make sure to follow the instructions after you click the link to confirm your account. Thank you, bye!")    
    print()

if __name__ == "__main__":
    main()


