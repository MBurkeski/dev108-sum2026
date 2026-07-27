# starting file for lab 6

import nameformat as myNames

def other():
  # welcome/greeting
  print("Testing module functions from nameformat")
  print("Let's call the module function!\n")

  # make a call to the module using the specified namespace defined in line 2 (myNames)
  myNames.testThis()
  print()
  print("--- Example Two ---")
  print("Let's call the module function and pass an argument.")
  while True:
    # a second example using an input and passing the input value to the function defined in the module 
    print("1 - Say Hello\n2 - Output Full Name\n3 - Output Last Name, First Name\n4 - Read Documentation\n5 - Exit")
    menu = (input("\nWhat is your choice? "))
    if menu.isdigit():
      menu = int(menu)
      if menu == 5:
        print("Thanks for playing!")
        break
      print()
      myNames.main()
    else:
      print("\n *** Sorry, invalid input. Please try again and input numbers 1-5 only! *** ")


if __name__ == "__other__":
  other()
 