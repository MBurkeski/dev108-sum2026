# starting file for lab 6

import nameformat as myNames


# main function
def main():
    while True:
        menu = int(input("\nWhat is your choice? "))
        if menu == 1:
            print("Hello " + myNames.first_name + "!")
            menu = int(menu)
        elif menu == 2:
            print(myNames.first_name, myNames.last_name)
        elif menu == 3:
            print(myNames.last_name + ", " + myNames.first_name)
        elif menu == 4:
            help(myNames.say_hello)
            help(myNames.full_name)
            help(myNames.last_name_first)
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