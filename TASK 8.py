BASE_RATE = 30.00
FAT_STEP_VALUE = 0.40
SNF_STEP_VALUE = 0.30

def rate_per_litre(fat, snf):
    fat_steps = round((fat - 3.5) / 0.1)
    snf_steps = round((snf - 8.5) / 0.1)
    return round(BASE_RATE + fat_steps * FAT_STEP_VALUE
                 + snf_steps * SNF_STEP_VALUE, 2)

def payout(litres, fat, snf):
    return round(litres * rate_per_litre(fat, snf), 2)

def ten_day_total(payments):
    return round(sum(payments), 2)

farmer_id = input("Enter Farmer ID: ")
total = 0.0

for day in range(1, 11):
    print("Day", day)
    litres = float(input("Enter litres: "))
    fat = float(input("Enter fat percentage: "))
    snf = float(input("Enter SNF percentage: "))

    if litres < 0 or not 2.0 <= fat <= 7.0 or snf < 0:
        print("Invalid input")
        continue

    rate = rate_per_litre(fat, snf)
    amount = payout(litres, fat, snf)
    total += amount

    print(f"Rate: Rs.{rate:.2f}")
    print(f"Payment: Rs.{amount:.2f}")

print(f"Farmer ID: {farmer_id}")
print(f"Ten-day total: Rs.{total:.2f}")