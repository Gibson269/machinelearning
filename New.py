### Map () Shopping Cart Discount System

# Step 1: Define item prices
item_prices = [30, 60, 100, 20, 75]  # Example prices

# Step 2: Apply discount using map()
def apply_discount(price):
    return price * 0.9 if price > 50 else price

discounted_prices = list(map(apply_discount, item_prices))

# Step 3: Calculate total bill
total = sum(discounted_prices)

# Step 4: Display results
print("Original Prices:", item_prices)
print("Discounted Prices:", discounted_prices)
print("Total Bill: $", total)

