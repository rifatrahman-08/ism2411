# Self - Asessment Questions

#1. The first mistake I noticed was that the code was not adding the sales correctly. I found it by looking through the code, which shows that I am improving at finding errors myself.
#2. apply_discount(price, tier) takes a price and discount level. It returns the price after the discount, and someone can use it if they know what to enter.
#3. AI helped me understand the code better by explaining my mistakes and how to fix them. It helped me learn instead of just giving me the answers.



# Exercise #1: 

def calculate_tax(price, rate):
    return price * rate


tax1 = calculate_tax(100, 0.07)
tax2 = calculate_tax(250, 0.08)

print(f"Tax for $100 at 7%: ${tax1:.2f}")
print(f"Tax for $250 at 8%: ${tax2:.2f}")


# Exercise 2:

def apply_discount(price, tier):
    if tier == "gold":
        return price * 0.85
    elif tier == "silver":
        return price * 0.90
    elif tier == "bronze":
        return price * 0.95
    else:
        return price

# Calling the function with different tiers
original_price = 200

for tier in ["gold", "silver", "bronze", "none"]:
    print(f"{tier}: ${apply_discount(original_price, tier):.2f}")

# Exercise 3: 

def final_price(price, tax_rate, discount_tier):
    discounted_price = apply_discount(price, discount_tier)
    tax = calculate_tax(discounted_price, tax_rate)
    return discounted_price + tax


# Calling the final_price function


print(f"final_price(200, 0.07, 'gold') = ${final_price(200, 0.07, 'gold'):.2f}")

# Exercise 4: 

orders = [(200, 'gold'), (150, 'silver'), (80, 'bronze'), (500, 'none')]


rate = 0.07
for price, tier in orders:
    total = final_price(price, rate, tier)
    print(f"Price: ${price} | Tier: {tier} | Total: ${total:.2f}")


# Exercise 5:

# fixed code
sales = [120, 80, 250, 175, 90]

# Calculate the total
total = 0
for sale in sales:
    total += sale
print(f"Total: ${total}")

# Count the sales
count = 0
for sale in sales:
    count += 1
print(f"Count: {count}")

# Print each sale
i = 0
while i < len(sales):
    print(sales[i])
    i += 1

# I fixed the total calculation, added a missing colon, and corrected the while loop condition to prevent an error.

# Exercise 6

x = 100   # global variable

def double_it():
    x = 999   # local variable
    return x * 2

print(x)
print(double_it())
print(x)

# The local variable x inside the function is separate from the global variable x. Therefore, the global x stays 100 even after the function runs.