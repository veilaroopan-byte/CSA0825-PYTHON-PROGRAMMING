# Constants
BASE_RATE = 30.0
FAT_RATE = 0.40
SNF_RATE = 0.30
MIN_FAT = 2.0
MAX_FAT = 7.0

# Variables
farmer_id = "F101"
litres = 10.0
fat = 4.0
snf = 8.0

# Calculate payment
rate = BASE_RATE + fat * FAT_RATE + snf * SNF_RATE
amount = litres * rate

print("Rate per litre:", rate)
print("Payment amount:", amount)

# Dynamic typing
x = 10
x = "Hello"
print("Dynamic typing:", x)

# Swapping variables
a, b = 10, 20
a, b = b, a
print("Swapped values:", a, b)