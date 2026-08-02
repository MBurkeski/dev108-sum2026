
# Name: Morgan Burke
# Assignment: Code Practice Lab 6 (Lab 6-2 Debug)
# Date: 7/28/2026


# display a welcome message and directions
print()
print("The Test Scores application")
print()

# set the default for the while loop to run the first time
again = "y"
while again.lower() == "y":

    print("Enter test scores")
    print("Enter 'x' to end input for test scores")
    print("======================")

                   
    # initialize variables
    counter = 0
    score_total = 0
    test_score = 0


    # get test scores from the user
    while test_score != 999:
        test_score = (input("Enter test score (or 'x' to end input): "))
        if test_score.lower() == "x":
            break
        else:
            # change the input to an float
            test_score = float(test_score)
            if test_score >= 0 and test_score <= 100:
                score_total += test_score
                counter += 1
            else:
                print("Test score must be from 0 through 100. Score discarded. Try again.")   


    # calculate average score
    average_score = (round(score_total / counter, 2))

    # format and display the result
    print("======================")
    print(f"Total Score: {score_total}")
    print(f"\nAverage Score: {average_score}")
    print()

    # ask the user if they want to calculate another set of test scores
    again = input("Would you like to calculate another set of test scores? (y/n): ")
    print()
print("No worries, have a nice day! Goodbye!")
print()
