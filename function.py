#Function definition
def calculate_discount(price,discount_percent):
    if discount_percent >= 20:
        return price - (price * discount_percent/100)
    else:
        return price
    

#Main program
#Ask for user input
price = float(input("Enter the original price:"))
discount_percent = float(input("Enter the discount percentage:"))

#Call the function
final_price = calculate_discount( price,discount_percent)

#Display result
print(f"The final price is :{final_price}")