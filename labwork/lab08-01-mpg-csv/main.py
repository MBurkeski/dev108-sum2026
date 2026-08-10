## Starting file for Exercise 7.1

# Morgan Burke
# Code Practice Lab 8 (exercise 7.1 & 7.2)
# 8/1/2026

# Instructions 7.1
# You will modify the Miles Per Gallon program so that it stores the input data for each calculation in a CSV file. Then you will use this program file to complete Exercise 7-2.  
# The program output will not need to have any edits made to the display input/output. Everything you add will be behind the scenes. 
# Review the code and run the program so that you understand the starting point. 
# Enhance the program so that it creates a simple two-dimensional list. You should be saving the distance, gallons, and calculated MPG in each row of the list. 
# Enhance the program so that it saves the data from the list (for all inputs) in a file named trips.csv. Do not save the data until the user is done inputting values. 
# Test the program to make sure it works. You can view the .csv file in Trinket's code editor or an associated program like Notepad or Excel if you are working with a local code editor on your computer.

# Instructions 7.2
# Continue to modify the Miles Per Gallon program so that it uses the CSV file created in Exercise 7-1.   
# follow the instructions in the book to create the following functions (page 229-230)
# write_trips() which is similar to the function created in program 1. Be sure to write the trip after every input. 
# read_trips() that will read the data in the existing trips.csv file and store to the trips list before asking for any additional inputs.
# list_trips() which will display the data in the trips list before adding any trips to the list.
# main() enhance to get data from the CSV file and so it adds the last trip that's entered to the trip list after it calculates the MGP then display the data for the updated trips list


import csv

# create a filename for our .csv file
filename = "trips.csv"

def write_trips(trip):
    with open(filename, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(trip)

def read_trips():
    trips= []
    with open(filename, newline="") as file:
        reader = csv.reader(file)
        for row in reader:
            trips.append(row)
    return trips

def list_trips(trips):
    print("Distance\tGallons\t\tMPG")
    for i in range(0, len(trips)):
        trip = trips[i]
        print(str(trip[0]) + "\t\t" + str(trip[1]) + "\t\t" + str(trip[2]))

def get_miles_driven():
    while True:
        miles_driven = float(input("Enter miles driven :     "))                    
        if miles_driven > 0:       
            return miles_driven
        else:
            print("Entry must be greater than zero. Please try again.\n")
            continue
    
def get_gallons_used():
    while True:
        gallons_used = float(input("Enter gallons of gas:     "))                    
        if gallons_used > 0:       
            return gallons_used
        else:
            print("Entry must be greater than zero. Please try again.\n")
            continue
        
def main():
    # display a welcome message
    print("The Miles Per Gallon application")
    print()

    trips = read_trips()
    list_trips(trips)

    more = "y"
    while more.lower() == "y":
        miles_driven = get_miles_driven()
        gallons_used = get_gallons_used()
                                 
        mpg = round((miles_driven / gallons_used), 2)
        print("Miles Per Gallon:\t" + str(mpg))
        print()

        # create a list for the 3 values of this calculation
        trip = []
        trip.append(miles_driven)
        trip.append(gallons_used)
        trip.append(mpg)

        # now append this entire row to my trips list
        trips.append(trip)
        
        # be sure to write this row of data before accepting more data
        write_trips(trip)

        list_trips(trips)
        more = input("More entries? (y or n): ")

    print("Bye")

if __name__ == "__main__":
    main()

