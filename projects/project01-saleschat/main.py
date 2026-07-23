# This is a placeholder for your code. No starter file is provided. 

# Follow the instructions and create comments for the
#  actions your program will perform. 


# Name: Morgan Burke
# Date: 7/21/2026
# Project Name: Programming Project 1: Fake "Sales ChatBot"


# Required Greeting, chatbot Name, 
print()
print("Hello, welcome to the exclusive SEAWHEEZE event gear website!")
print()
print("I am your personal shopper assistant,\nyou can call me Pal.") 
print()

# Product prompt inital entry question
entryQuestion = input("Would you like to learn more about our new running gear\nexclusive for members only? (y/n) ")
if entryQuestion.lower() == "y":
    print()
    print("Yay! Let's get started.")
    print()
    print()
    print("This year we have several styles ready to accompany you on your next PR!\nSince the 2026 SEAWHEEZE Half Marathon is in Vancouver, British Columbia,\nwe wanted to make sure you stay cool this August and represent the US in style.\nEach of the items are featured in exclusive colors for this event,\nnone of these items can be found in the store,\nso online purchases only.")
    print()
    print()
    print("Little bit about our new shorts:")
    print("Our new elite 5 inch running shorts\nhave built in underwear briefs\nmade with sustainably sourced cotton\nthat has moisture wicking abilities and\nantimicrobial properities to help you stay clean\nand dry on your long runs ahead.\nThese shorts also have a thick elastic band\nso the shorts fit perfectly on every pair of hips.\nThe butter soft material of these shorts\nwill make it hard to take them off\nand the softness will be maintained with every wash.")
    print()
    print("Price is regularly $90 plus tax, but if ordered today, the price is only $50 plus tax.")
    print()
    
    # purchase offer for shorts
    purchaseOffer = input("Would you like to try these exclusive shorts out for a test run? (y/n) ")
    if purchaseOffer.lower() == "y":
        print()
        print("Yay!!\nLet's proceed with your order details below.")
        print()
        print()
        runnerSize = input("What size are you running in these days? ")
        print("You entered", runnerSize,".")
        print()

        # closing the sale details
        print("To finish your order, we need a few more details.")
        name = input("What is your first and last name? ")
        print()
        email = input("What is your email address? ")
        print()
        phone = input("What is your phone number? ")
        print()
        quantity = 0    # initialize the variable for calculating total cost
        quantity = int(input("How many shorts would you like to purchase today? (1, 2, 3, etc.) "))
        print()
        print()

        # calculate total
        shortPrice = 50     # initialize the variable
        taxRate = 0.10      # initialize the variable
        subTotal = quantity * shortPrice
        print(f"Sub Total: {quantity} x {shortPrice} = ${subTotal: .2f}")   # calculation of sub total
        print(f"plus 10 percent sales tax")
        print("======================")
        totalDue = subTotal * (1 + taxRate)     # calculation of total amount due
        print(f"Total Amount Due: ${totalDue:.2f}")     
        print()
        print()

        # question to continue with the transaction
        purchaseQuestion = input("Would you like to continue?(y/n) ")
        if purchaseQuestion.lower() == "y":
            print()
            print("Yay! Please see your receipt below.")
            print()

            # receipt from purchase
            print("Purchase Receipt: ")
            print("======================")
            print(name)
            print(email)
            print(phone)
            print("Payment method via account details")
            print("======================")
            print("Item(s) Description: Elite 5 inch running shorts\nColor: SEAWHEEZE Exclusive")
            print("Size(s): ", runnerSize)
            print("Quantity: ", quantity)
            print("======================")
            print(f"Total Amount Paid: ${totalDue:.2f}")
            print()
            print()

            # farewell thank you message
            print("Thank you for your purchase,\nand best of luck to you in your next race.\nI feel a PR loading!")
            print()

        # no response to continuing with the purchase
        elif purchaseQuestion.lower() == "n":   
            print()
            print("Darn, maybe next time. Happy running!")

        # any other response whether to purchase or not
        else:   
            print()
            print("Invalid response entry.\nPlease reanswer the question with a Y for yes\nor a N for no.\nThank you.")
            print()

    # no response to offer of purchase
    elif purchaseOffer.lower() == "n":
        print()
        print("Darn, maybe next time. Happy running!")

    # other response to purchase
    else:
        print()
        print("Oops invalid entry.\nPlease try again.\nPlease reanswer the question with a Y for yes\nor a N for no.\nThank you.")


# Response of "no" to the entry question
elif entryQuestion.lower() == "n":
    print()
    print("No worries, feel free to shop away on your own.\nIf at any point you need help,\nI will be here in the chatbox\nready if you need your Pal.")
    print()

# Other response to the entry question
else:
    print()
    print("Invalid response entry.\nPlease reanswer the question with a Y for yes\nor a N for no.\nThank you.")
    print()

