class Product:
    def __init__(self, name, price=0, quantity=0):
        self.name = name
        self.price = price
        self.quantity = quantity

    def calculate_total(self):
        return self.price * self.quantity

class Cart:
    def __init__(self):
        self.cart = []  

    def add_to_cart(self, product):
        self.cart.append({
            "Product Name": product.name,
            "Price": product.price,
            "Quantity": product.quantity,
            "Total": product.calculate_total()
        })
        print(f"✅ {product.name} added to cart!")

    def display_cart(self):
        if not self.cart:
            print("🛒 Your cart is empty!")
            return
        print("\n🛍️ Your Shopping Cart:")
        for item in self.cart:
            print(f"{item['Product Name']} - {item['Quantity']} x ${item['Price']} = ${item['Total']}")
    
    def checkout(self):
        if not self.cart:
            print("⚠️ Your cart is empty. Add items before checkout!")
            return

        print("\n🧾 Checkout Receipt:")
        total_bill = 0
        for item in self.cart:
            print(f"{item['Product Name']} - {item['Quantity']} x ${item['Price']} = ${item['Total']}")
            total_bill += item['Total']
        
        print(f"\n💳 Total Bill: ${total_bill:.2f}")
        self.cart.clear()  
        print("✅ Purchase complete! Your cart is now empty.")

def main():
    shopping_cart = Cart()
    
    while True:
        print("\n🛒 Shopping Cart System")
        print("1️⃣ Add Product")
        print("2️⃣ View Cart")
        print("3️⃣ Checkout")
        print("4️⃣ Exit")
    
        choice = input("Select an option: ")

        if choice == "1":
            name = input("Enter product name: ")
            price = float(input("Enter product price: "))
            quantity = int(input("Enter quantity: "))
            product = Product(name, price, quantity)
            shopping_cart.add_to_cart(product)

        elif choice == "2":
            shopping_cart.display_cart()

        elif choice == "3":
            shopping_cart.checkout()

        elif choice == "4":
            print("👋 Exiting... Thank you for shopping!")
            break

        else:
            print("❌ Invalid input! Please try again.")

if __name__ == "__main__":
    main()
