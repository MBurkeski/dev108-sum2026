# Final Project - Morgan Burke

# Option: Character Generator Battle Simulator 

# Directions for final project:
Before you submit, check that you:
1. added your name, date, class number, and project name to your code
2. included test case data for at least 3 inputs and fixed any errors that came up (you can create a separate file in Trinket called README.md and type your information directly into it. - see example below
3. commented your code - at minimum, describe each function
4. started your program using a main function
5. applied formatting to your input and output
6. checked for typos/spelling errors
7. You will submit a Trinket URL for this homework assignment (preferable) or all files associated with your program (including all .py files, .csv files, and the README.md file, and a list of any modules that you had to install for your program to work). 
8. Be sure that your program is running free of errors before submitting it.

Test Results
-Test it with different inputs and make sure your inputs are being stored as the correct data type. Include test data and outcomes for at least THREE different inputs within your program code within a README.md file.
-Just a reminder - your code must be written 100% by you. Only use concepts we have used so far in this class. Any code that you include in your program that we have not covered in this course should be discussed with me first so that I know you are writing the code yourself. Don't overcomplicate the assignment. 

AI Disclosure
You are required to disclose all usage of AI tools used to learn, assist, debug, document, and improve code. Identify which tools you used and how you used the tool for your project, if anything. 

Final Project Deliverables
1. Working Python program - well structure code, naming conventions, proper syntax, free of syntax and logical errors, user experience, and program execution.
2. Documentation for test case data in the README.md file.
3. AI disclosure - can also be included in the README.md file.
4. Be sure to submit a working program free of errors.
5. Upload all of your files to the Canvas submission AND post a link to your Github REPO.  
**Note: Any project missing the README.md file and the above deliverables will receive 0 points for those items. You will NOT be contacted nor given the opportunity to resolve the issue due to this being the final project and the class is coming to an end. 


# Test Results - three test cases
Outputs:

1. Test Case #1 - list input
====================================================================================================
Welcome to the Character Generator Battle Simulator - Fantasy Edition
====================================================================================================


This program is a battle simulator where the user is able to
create random fantasy characters to face off with one another
to earn the hero title. You have the option to create your own character
or the program will create one for you. May the odds be ever in your favor...

Before we get started, what is your name? Morgan

Hello, Morgan! Welcome to the battleground!

**********PLAYER MENU**********
1. List all characters
2. Add a character
3. Delete a character
4. Find a character
5. Play a battle
6. Exit

Please choose an option (1-6): 1

Current Character List:

No.  NAME           TYPE                STRENGTH    INTELLECT   CHARISMA    SPEED     HIT POINTS  WINS    LOSSES  
----------------------------------------------------------------------------------------------------------------------------
1    Shadow         Human Warrior       18          12          15          18        55          1       0       
2    Blaze          Dragon Rider        21          11          14          16        60          2       1       
3    Ragnar         Troll Princess      19          8           11          9         58          0       0       
4    Nova           Wizard              10          20          18          13        45          0       1       
5    Ember          Elf Archer          15          17          16          20        50          0       0       
6    Spirit         Mystical Fairy      8           19          20          18        40          0       1       
7    Gandalf        Dragon Rider        12          14          10          19        59          1       1       


**********PLAYER MENU**********
1. List all characters
2. Add a character
3. Delete a character
4. Find a character
5. Play a battle
6. Exit

Please choose an option (1-6): 

2. Test Case #2 - delete an input
Please choose an option (1-6): 3
Enter the name of the character you want to delete: Gandalf

You selected: Gandalf
Are you sure you want to delete this character? (y/n): y

Gandalf was deleted successfully.

**********PLAYER MENU**********
1. List all characters
2. Add a character
3. Delete a character
4. Find a character
5. Play a battle
6. Exit

Please choose an option (1-6): 

3. Test Case #3 - search for a deleted input
Please choose an option (1-6): 4
Character Name: Gandalf

No character named 'Gandalf' was found.



**********PLAYER MENU**********
1. List all characters
2. Add a character
3. Delete a character
4. Find a character
5. Play a battle
6. Exit

Please choose an option (1-6): 

4. Test Case #4 - revised list input
Please choose an option (1-6): 1

Current Character List:

No.  NAME           TYPE                STRENGTH    INTELLECT   CHARISMA    SPEED     HIT POINTS  WINS    LOSSES  
----------------------------------------------------------------------------------------------------------------------------
1    Shadow         Human Warrior       18          12          15          18        55          1       0       
2    Blaze          Dragon Rider        21          11          14          16        60          2       1       
3    Ragnar         Troll Princess      19          8           11          9         58          0       0       
4    Nova           Wizard              10          20          18          13        45          0       1       
5    Ember          Elf Archer          15          17          16          20        50          0       0       
6    Spirit         Mystical Fairy      8           19          20          18        40          0       1       


**********PLAYER MENU**********
1. List all characters
2. Add a character
3. Delete a character
4. Find a character
5. Play a battle
6. Exit

Please choose an option (1-6): 

5. Test Case #5 - exit input
Please choose an option (1-6): 6

Thank you for playing, Morgan!
Best of luck in your future battles!

Just remember, you are a hero to us regardless of your battle outcomes. Bye!!

6. Test Case #6 - invalid input
====================================================================================================
Welcome to the Character Generator Battle Simulator - Fantasy Edition
====================================================================================================


This program is a battle simulator where the user is able to
create random fantasy characters to face off with one another
to earn the hero title. You have the option to create your own character
or the program will create one for you. May the odds be ever in your favor...

Before we get started, what is your name? Morgan

Hello, Morgan! Welcome to the battleground!

**********PLAYER MENU**********
1. List all characters
2. Add a character
3. Delete a character
4. Find a character
5. Play a battle
6. Exit

Please choose an option (1-6): Morgan

Invalid choice. Please enter a number from 1 to 6.

**********PLAYER MENU**********
1. List all characters
2. Add a character
3. Delete a character
4. Find a character
5. Play a battle
6. Exit

Please choose an option (1-6): 


# AI Disclosure
ChatGPT was used to help me work out some bugs. I had trouble reformatting my battle sequence and kept getting an error with the time module. I also used it to help me reformat my CSV creation, I originally created a secon main.py file to just create the CSV like we had done with the assignment to show the two different ouputs, but I decided to try to keep it all in one and was getting an error when trying to list all the characters, it pointed out my indentation errors. It also made some suggestions on formatting my code differently so it read better.

# Link to Github Repo
https://github.com/MBurkeski/dev108-sum2026/tree/main/final

# Link to permalink
https://github.com/MBurkeski/dev108-sum2026/tree/004bdb3d9a939b6b1856e44dd978f3fe2d1250d0/final

# Additional Info:
I reviewed the suggestions from the discussion board on the project 3 since this is a modification of that project. It took me forever to make so it made more sense to modify that code to save time creating this one.
I added a better description and created options for the user to choose from if they didn't want to create thier own. 