# Constants
MIN_FAT = 2.0
MAX_FAT = 7.0
TOTAL_DAYS = 10

# Input
farmer_id = input("Enter Farmer ID: ")
litres = float(input("Enter milk quantity in litres: "))
fat = float(input("Enter fat percentage: "))
snf = float(input("Enter SNF percentage: "))
shift = input("Enter shift (Morning/Evening): ")

# Validation
if litres < 0:
    print("Invalid milk quantity")
elif not MIN_FAT <= fat <= MAX_FAT:
    print("Invalid fat percentage")
elif snf < 0:
    print("Invalid SNF percentage")
else:
    # Example rate calculation
    rate = 30 + (fat * 2) + (snf * 0.5)
    amount = litres * rate
    ten_day_total = amount * TOTAL_DAYS

    print("Farmer ID:", farmer_id)
    print("Shift:", shift)
    print("Rate per litre:", round(rate, 2))
    print("Payment amount:", round(amount, 2))
    print("Ten-day total:", round(ten_day_total, 2)) 