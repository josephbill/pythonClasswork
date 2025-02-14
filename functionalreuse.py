"""
FUNCTIONAL REUSABILITY
You're building an e-commerce order processing system,
 and you need to calculate discounts, taxes, and final prices
for multiple products. Instead of writing the same logic repeatedly,
you'll create reusable functions.
"""
price = int(input("Enter price: "))
discount = int(input("Enter discount percentage: "))
# function to give discount
def apply_discount(p, d):
    """applies a discount to a price and returns the new price"""
    discount_price = (p * d/ 100)
    return p - discount_price

# print(apply_discount(price,discount))
# function to calculate tax after discount application
def calculate_taxes(price):
    """calculates the tax on a given price """
    vattax = 16
    result = price * (vattax / 100)
    return result

# THIS FUNCTION WILL THEN GET OUR FINAL PRICE
def get_final_price(price,discount):
    """calculate the final price (discount price + tax)"""
    discountedPrice = apply_discount(price,discount)
    tax = calculate_taxes(discountedPrice)
    result_price = discountedPrice + tax
    return (f"The item discount price {discountedPrice} it has a tax"
            f"of {tax} so the final price is {result_price}")

print(get_final_price(price,discount))


"""
PROGRAM 2: 
Scenario:
You're building a banking application where users can deposit,
 withdraw, and check balances.
  Instead of writing these operations multiple times, 
  you'll create reusable functions.
"""
amount = 0
balance = int(input("Enter Balance: "))
# deposit function
def deposit(balance, amount):
    result = balance + amount
    return result

# WITHDRAWAL
def withdraw():
    withdrawal_amount = int(input("Enter withdrawal amount: "))
    current_balance = deposit(balance, amount)
    if current_balance < withdrawal_amount:
        return "Insufficient funds"
    else:
        available_balance = current_balance - withdrawal_amount
        return (f"Withdrawal success {withdrawal_amount} balance was at"
                f"{current_balance} new balance {available_balance}")

print(withdraw())























































