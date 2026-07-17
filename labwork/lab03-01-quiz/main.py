# Create a simple 5 question math or multiple choice quiz following the instructions provided

# Name: Morgan Burke
# Date: 7/16/2026
# Practice Lab 3-1 

# 1. Title: Random Trivia Questions
print()
print("Welcome to Random Trivia Questions!")
print()

# 2. Question the user whether they would like to take the quiz
print()
entryQuestion = input("Would you like to proceed to the quiz? Please enter either: y/n ")
if entryQuestion.lower() == "y":
      print("Yay! Please proceed to the first question.")
      print("Directions: Please type out the full answer, for example A. This is my answer.")
      print("Good luck!")

      # 3. Initialize a score counter variable
      counter = 0

      # 4. Five Quiz Questions 
      # question one
      print()
      print("Question One: How many cards are in a standard deck of playing cards?")
      print("A. 23")
      print("B. 52")
      print("C. 46")
      print()
      questionOne = input("Your answer to question one: ")
      if questionOne == "B. 52":
            print("Great job! You are correct!")
            counter += 1
      else:
            print("Oops! Sorry, that answer is incorrect. The correct answer is B. 52 cards.")
      print()

      # question two
      print("Question Two: What is the only planet in our solar system that rotates clockwise on its axis?")
      print("A. Venus")
      print("B. Neptune")
      print("C. Earth")
      print()
      questionTwo = input("Your answer to question two: ")
      if questionTwo == "A. Venus":
            print("Great job! You are correct!")
            counter += 1
      else:
            print("Oops! Sorry, that answer is incorrect. The correct answer is A. Venus.")
      print()
       
      # question three
      print("Question Three: What freezes the fastest?")
      print("A. Cold water")
      print("B. Hot water")
      print()
      questionThree = input("Your answer to question three: ")
      if questionThree == "B. Hot water":
            print("Great job! You are correct!")
            counter += 1
      else:
            print("Oops! Sorry, that answer is incorrect. The correct answer is B. Hot water.")
      print()

      # question four
      print("Question Four: In human anatomy, which body part does the hallux refer to?")
      print("A. The heel")
      print("B. The elbow")
      print("C. The big toe")
      print()
      questionFour = input("Your answer to question four: ")
      if questionFour == "C. The big toe":
            print("Great job! You are correct!")
            counter += 1
      else:
            print("Oops! Sorry, that answer is incorrect. The correct answer is C. The big toe.")
      print()

      # question five
      print("Question Five: Which branch of the U.S. armed forces uses the slogan - It's not a job, it's an adventure ?")
      print("A. The Air Force")
      print("B. The Army")
      print("C. The Navy")
      print()
      questionFive = input("Your answer to question five: ")
      if questionFive == "C. The Navy":
            print("Great job! You are correct!")
            counter += 1
      else:
            print("Oops! Sorry, that answer is incorrect. The correct answer is C. The Navy.")
      print()

      # 5. User Total Score
      print("Your score is: ", + counter)

      # 6. Feedback on test results
      if counter == 5:
            print("Fantastic work! You are a rockstar!")
      elif counter == 4:
            print("Well done. You are so close to 100%")
      elif counter == 3 or 2:
            print("Hey, you know some things! Now you know what you need to study up on for trivia night.")
      elif counter == 1 or 0:
            print("Yikes. Trivia might not be your thing. Thanks for trying.")
      print()

      # 7. Quiz farewell message
      print()
      print("Congratulations for finishing the Quiz. Regardless of your score, you should be proud of yourself for completing it! Best of luck to you! Goodbye.")
      print()
# no response to do the quiz
elif entryQuestion.lower() == "n":
      print("Well, no fun to be had for you. Maybe next time. Goodbye.")
      print()

# any other response to 
else:
      print("Invalid entry. Please restart.")








