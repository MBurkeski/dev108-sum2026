# Starting file for Exercise 3-1

# Morgan Burke
# 7/22/2026
# Exercise 3-1: Enhance the Miles Per Gallon Program

# display a welcome message
print()
print("The Miles Per Gallon application")
print()

# get input from the user
miles_driven = float(input("Enter miles driven: "))
gallons_used = float(input("Enter gallons of gas used: "))
gallons_cost = float(input("Enter cost per gallon: "))
print()

if miles_driven <= 0:
    print("Miles driven must be greater than zero. Please try again.")
elif gallons_used <= 0:
    print("Gallons used must be greater than zero. Please try again.")
else:
    # inputs must be good
    # calculate and display miles per gallon
    mpg = round((miles_driven / gallons_used), 2)
    print("Miles Per Gallon: ", mpg)
    tgc = round((gallons_used * gallons_cost), 2)        # total gas cost
    print("Total Gas Cost: ", tgc)
    cpm = round((tgc / miles_driven), 2)           # cost per gmile
    print("Cost Per Mile: ", cpm)
    # while loop 
    while True:
        print()
        again = input("Would you like to calculate the miles per gallon for another trip? (y/n) ")
        print()
        if again.lower() == "y":
            # run through the inputs
            miles_driven = float(input("Enter miles driven: "))
            gallons_used = float(input("Enter gallons of gas used: "))
            gallons_cost = float(input("Enter cost per gallon: "))
            print()
            # calculate and display miles per gallon
            mpg = round((miles_driven / gallons_used), 2)
            print("Miles Per Gallon: ", mpg)
            tgc = round((gallons_used * gallons_cost), 2)        # total gas cost
            print("Total Gas Cost: ", tgc)
            cpg = round((tgc / miles_driven), 2)           # cost per gallon
            print("Cost Per Gallon: ", cpg)
            continue
        else:
            # exit the program
            print("Thank you for your participation.")
            break
print()
print("Bye")

