# Code Practice Lab 9
# Name: Morgan Burke
# 8/12/2026

# instructions:
# x You will modify the Invoice program so that the program formats currency values correctly.
# x You will also add and calculate a shipping cost to the output. 
# x Review the code and run the program so that you understand the starting point. 
# x Modify the program so that it displays the order total and invoice total as U.S. currency values with dollar signs and two decimal points.
# x Add a shipping cost which should be 8.5% (.085) of the subtotal. 
# x Use the decimal module to make sure each monetary value has the correct number of decimal places. 
# x Be sure that your decimal places line up nice like in the example below.
# X Ensure that you have a title/greeting in your output. 
# X Be sure to have an exit message too. 
# x For the locale statement, you'll want to use something like: locale.setlocale(locale.LC_ALL, ' ')  


from decimal import Decimal
from decimal import ROUND_HALF_UP
import locale as lc

#set U.S. currency format
lc.setlocale(lc.LC_ALL, "") 

# display welcome and title
print()
print("Hello, welcome to the Invoice Program!")
print("This program creates a invoice for an order total that you input.")
print("-" * 100)
print()
print("The Invoice program")

# if the answer to continue is yes with a "y", loop to continue
choice = "y"
while choice == "y":
    
    # get the user entry
    order_total = Decimal(input("Enter order total: "))
    order_total = order_total.quantize(Decimal("1.00"), ROUND_HALF_UP)            

    # determine the discount percent
    if order_total > 0 and order_total < 100:
        discount_percent = Decimal("0")
    elif order_total >= 100 and order_total < 250:
        discount_percent = Decimal(".1")
    elif order_total >= 250:
        discount_percent = Decimal(".2")

    # calculate the results
    discount = order_total * discount_percent
    discount = discount.quantize(Decimal("1.00"), ROUND_HALF_UP)      

    subtotal = order_total - discount
    subtotal = subtotal.quantize(Decimal("1.00"), ROUND_HALF_UP)

    shipping_cost = subtotal * Decimal("0.085")
    shipping_cost = shipping_cost.quantize(Decimal("1.00"), ROUND_HALF_UP)

    tax_percent = Decimal(".05")
    sales_tax = subtotal * tax_percent
    sales_tax = sales_tax.quantize(Decimal("1.00"), ROUND_HALF_UP)  

    invoice_total = subtotal + sales_tax + shipping_cost
    invoice_total = invoice_total.quantize(Decimal("1.00"), ROUND_HALF_UP)


    # display the results
    print(f"Order total:            ${order_total:>12,.2f}")
    print(f"Discount amount:        {discount:>13,.2f}")
    print(f"Subtotal:               {subtotal:>13,.2f}")
    print(f"Shipping cost:          {shipping_cost:>13,.2f}")
    print(f"Sales tax:              {sales_tax:>13,.2f}")
    print(f"Invoice total:          ${invoice_total:>12,.2f}")
    print()

    choice = input("Would you like to continue? (y/n): ")    
    print()

print("Thank you, bye!")
