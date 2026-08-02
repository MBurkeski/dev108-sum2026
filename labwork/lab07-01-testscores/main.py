# Starting file for Exercise 6.1 in our textbook

# Name: Morgan Burke
# Code Practice Lab 7 (exercise 6.1)
# 8/1/2026

# Modify get_score() function to return a list of scores instead of the score total and count. X
# Modify process_scores() so the scores list is the only arugment. Use the len() function to get the number of scores in the list.
# Modify the main() function so the list returned by the get_score() function is stored in a variable. X
# Modify the process_score() function so it passes the scores list to it.
# Modify the process_score function to calculate the score total, number of scores, average score, low score, high score, and median score.
# Be sure to follow the exact instructions in our textbook, page 199* not 193

import statistics

def display_welcome():
    print()
    print("The Test Scores program")
    print("Enter test scores from 0 through 100.")
    print("Enter 'x' to exit")
    print("")

def get_scores():
   scores = []
   while True:
        score = input("Enter test score: (or 'x' to exit): ")
        if score == "x":
            return  scores
        else:
            score = int(score)
            if score >= 0 and score <= 100:
                scores.append(score)
            else:
                print("Test score must be from 0 through 100. " +
                      "Score discarded. Try again.")

def process_scores(scores):
    score_total = 0
    for thisscore in scores:    # page 169 recommended this format
        score_total += thisscore

    average_score = round(score_total / len(scores))

    median = round(statistics.median(scores)) # use the statistics module to calculate the median
    
    # format and display the result
    print()
    print("Total Score:       ", score_total)
    print("Number of Scores:  ", len(scores))
    print("Average Score:     ", average_score) 
    print("Lowest Score:      ", min(scores))
    print("Highest Score:     ", max(scores))
    print("Median Score:      ", median)
    
def main():
    display_welcome()
    scores = get_scores()
    process_scores(scores)
    print("")
    print("Bye!")

# if started as the main module, call the main function
if __name__ == "__main__":
    main()
