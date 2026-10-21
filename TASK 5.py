try:
    farmer_id = input("Enter Farmer ID: ")
    litres = float(input("Enter litres: "))
    fat = float(input("Enter fat percentage: "))
    snf = float(input("Enter SNF percentage: "))

    print(f"Farmer ID: {farmer_id}")
    print(f"Litres: {litres:.2f}")
    print(f"Fat: {fat:.2f}%")
    print(f"SNF: {snf:.2f}%")

except ValueError:
    print("Invalid input! Enter numbers correctly.")