# starting file for Exercise 3-2

# Morgan Burke
# 7/22/2026
# Exercise 3-2: Enhance the Test Scores Program

# be sure to follow along with my video demonstration video in our Canvas assignment instructions if you need help

#instructions
# Modify the program so that when the user enters "end" it ends the set of score entries and outputs the Total and Average Score for the set that was just finished. 
# Then ask if there is another set of test scores to enter. 
# Be sure to keep the validation for the number input to be between 0 and 100.


# display a welcome message
print("The Test Scores application")
print()

# set the defauly for the while loop to run the first time
repeat_test_scores = "y"
while repeat_test_scores.lower() == "y":

    print("Enter test scores")
    print("Enter end to end input")
    print("======================")

    # initialize variables
    counter = 0
    score_total = 0
    test_score = 0

    while test_score != 999:
        test_score = (input("Enter test score or end to end input: "))
        if test_score.lower() == "end":
            break
        else: 
            # change the input to an integer
            test_score = int(test_score)
            if test_score >= 0 and test_score <= 100:
                score_total += test_score
                counter += 1
            else:
                print("Test score must be from 0 through 100. Score discarded. Try again.")

    # calculate average score
    average_score = round(score_total / counter)
                    
    # format and display the result
    print("======================")
    print("Total Score:", score_total, "\nAverage Score:", average_score)
    print()
    repeat_test_scores = input("Would you like to enter another set of test scores? (y/n) ")

print("Goodbye, thank you for using the test scores program!")
