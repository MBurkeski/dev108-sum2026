
# Name: Morgan Burke (backup)
# Assignment: Code Practice Lab 6 (Lab 6-2 Debug)
# Date: 7/28/2026


# display a welcome message
print("The Test Scores application")
print()
print("Enter test scores")
print("Enter '999' to end input")
print("======================")

# initialize variables
counter = 0
score_total = 0
test_score = 0

while True:
    test_score = input("Enter test score (or 'x' to quit): ")
    if test_score != "x":
        test_score = int(test_score)
        counter += 1
    else:
        break
    if test_score >= 0 and test_score <= 100:
        score_total += test_score
        counter += 1

        # loop to ask for additional test scores to be run
        while True:
            print()
            again = input("Would you like to calculate another set of test scores? (y/n): ")
            if again.lower() == "y":
                # run through inputs
                print()
                test_score = float(input("Enter test score (or '999' to quit): "))
                if test_score >= 0 and test_score <= 100:
                    score_total += test_score
                    counter += 1
                elif test_score == 999:
                    # exit the program
                    print("Thank you for your participation.")
                    break
                else:
                    print("Test score must be from 0 through 100. Score discarded. Try again.")   
            else:
                # exit the program
                print("Thank you for your participation.")
                break      
            
        # calculate average score
        average_score = round(score_total / counter)
                
        # format and display the result
        print("======================")
        print("Total Score:", score_total,
        "\nAverage Score:", average_score)    
        
    elif test_score == 999:
        break
    else:
        print("Test score must be from 0 through 100. Score discarded. Try again.")   

# calculate average score
average_score = round(score_total / counter)
                
# format and display the result
print("======================")
print("Total Score:", score_total,
      "\nAverage Score:", average_score)
print()
print("Bye!")
