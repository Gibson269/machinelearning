class ComplexNumber:
    def __init__(self, x, y):
        self.x = x  # Real part
        self.y = y  # Imaginary part

    def __add__(self, other):
        return ComplexNumber(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return ComplexNumber(self.x - other.x, self.y - other.y)

    def __mul__(self, other):
        real_part = (self.x * other.x) - (self.y * other.y)
        imag_part = (self.x * other.y) + (self.y * other.x)
        return ComplexNumber(real_part, imag_part)

    def __truediv__(self, other):
        denominator = (other.x ** 2) + (other.y ** 2)
        if denominator == 0:
            raise ValueError("Division by zero is not allowed!")
        real_part = ((self.x * other.x) + (self.y * other.y)) / denominator
        imag_part = ((self.y * other.x) - (self.x * other.y)) / denominator
        return ComplexNumber(round(real_part, 2), round(imag_part, 2))

    def __repr__(self):
        return f"({self.x} + {self.y}i)"  # Represents complex number in standard form

# Function to get user input
def get_complex_input(prompt):
    real = float(input(f"Enter real part of {prompt}: "))
    imag = float(input(f"Enter imaginary part of {prompt}: "))
    return ComplexNumber(real, imag)

# Taking input from user
print("\n🔢 Complex Number Operations 🔢\n")
complex1 = get_complex_input("first complex number")
complex2 = get_complex_input("second complex number")

# Performing operations
print("\n📌 Results 📌")
print("➕ Addition:", complex1 + complex2)
print("➖ Subtraction:", complex1 - complex2)
print("✖️ Multiplication:", complex1 * complex2)
try:
    print("➗ Division:", complex1 / complex2)
except ValueError as e:
    print("❌", e)  # Handles division by zero

print("\n✅ Operations completed successfully!")
