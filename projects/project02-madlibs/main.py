# Placeholder for Madlibs main.py file

# Name: Morgan Burke
# Date: 7/26/2026
# Programming Project 2: Mad Libs

# Instructions
# X Output a title for the game.
# X Ask if the user would like to play a game.
# X Ask for the players name. Greet the player.
# X Ask the player to choose from TWO story ideas you have created.  Use an if statement here to separate the code for each choice.
# X Ask the player to input between 6 to 10 names/words/numbers to fill in spots for your story. Please do not go over 10 inputs because it can get very long to run/test the programs! 
# Create a short story to go along with the gameplay, substituting their inputted words into the story. Each story should be different and ask for different inputs. Do not reuse the same inputs for each story please. Your stories should be at a minimum of 4 sentences. 
# Ask if the user would like to play again (use a loop for this). Validate the user input as being y/n. If they input something that is NOT one of your options, ask the player to try again. 
# Validate the user input for the story selection. If they input something that is NOT one of your options, ask the player to try again. 
# Create a counter to record how many stories they have created. Display the counter before asking if they would like to play again. 


# Mad lib title
print()
def title():
    print("Welcome to the Nurse Mad Lib Game")
    print()


# ask to play
def play_ask():
    while True:
        initial_ask = input("would you like to play? (y/n)")
        if initial_ask.lower() == "y":
            print("Yay! Let's get started.") 
        elif initial_ask.lower() == "n":
            print("Darn, maybe next time. Bye!")
        else:
            print("Invalid entry please use a Y for yes and a N for no to play the Nurse Mad Lib Game.")


# get player name and greet player
def get_name():
    player_name = input("What is your first name? ")
    print("Hello," + player_name + "!")
    print()


# player chooses storyline
def story_line():
    print("What story line would you like to play?")
    print("a. Med Surg\n b. Emergency Department ")
    story_options = input("what story line did you choose? (a or b)")
    if story_line.lower() == "a":
        adjective1 = input("Please provide an adjective: ")
        name = input("Please provide a name: ")
        adjective2 = input("Please provide an adjective: ")
        number = input("Please provide a number: ")
        plural_noun = input("Please provide a plural noun: ")
        noun = input("Please provide a noun: ")
        verb = input("Please provide a verb: ")
    elif story_line.lower() == "b":
        adjective1 = input("Please provide an adjective: ")
        name = input("Please provide a name: ")
        number = input("Please provide a number: ")
        adjective2 = input("Please provide an adjective: ")
        noun = input("Please provide a noun: ")
        adjective3 = input("Please provide an adjective: ")
        plural_noun = input("Please provide a plural noun: ")
    else:
        ("Invalid entry, story line a or b are the only options. Please try again.")


def main():
    title
    play_ask
    get_name
    story_line
    # initialize variables
    again = "y"
    while again.lower() == "y":
            again = input("Would you like to play again? (y/n): ")
            print()
    print("No, worries. Have a nice day! Bye!")
    

# if started as the main module, call the main function
if __name__ == "__main__":
    main()