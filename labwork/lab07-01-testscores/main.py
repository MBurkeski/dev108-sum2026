# Starting file for Exercise 6.1 in our textbook

# Name: Morgan Burke
# Code Practice Lab 7 (exercise 6.1)
# 8/1/2026

# In this activity, you will modify the Test Scores program to store the score inputs in a list format. 
# You will also display some other statistics that you are able to calculate with the list values including:
# number of scores, low score, high score and median score. 
# Be sure to follow the exact instructions in our textbook, page 193:
# to make modifications to the get_scores() function, process_scores() function, and main() function.

def display_welcome():
    print("The Test Scores program")
    print("Enter 'x' to exit")
    print("")

def get_scores():
    score_total = 0
    counter = 0
    while True:
        score = input("Enter test score: ")
        if score == "x":
            return  score_total, counter
        else:
            score = int(score)
            if score >= 0 and score <= 100:
                score_total += score
                counter += 1 
            else:
                print("Test score must be from 0 through 100. " +
                      "Score discarded. Try again.")

def process_scores(score_total, count):
    # calculate average score
    average = score_total / count
                
    # format and display the result
    print()
    print("Score total:       ", score_total)
    print("Number of Scores:  ", count)
    print("Average Score:     ", average)

def main():
    display_welcome()
    score_total, count = get_scores()
    process_scores(score_total, count)
    print("")
    print("Bye!")

# if started as the main module, call the main function
if __name__ == "__main__":
    main()
