BASE_RATE = 30.0
FAT_RATE = 0.40
SNF_RATE = 0.30

def rate_per_litre(fat, snf):
    """Calculate milk rate per litre."""
    return BASE_RATE + (fat - 3.5) * FAT_RATE / 0.1 + (snf - 8.5) * SNF_RATE / 0.1

def payout(litres, fat, snf):
    """Calculate payment for milk supplied."""
    return litres * rate_per_litre(fat, snf)

def ten_day_total(payments):
    """Calculate total payment for ten days."""
    return sum(payments)

amount = payout(10, 4.2, 8.5)
total = ten_day_total([amount] * 10)

print("Rate per litre:", rate_per_litre(4.2, 8.5))
print("Payment:", round(amount, 2))
print("Ten-day total:", round(total, 2)) 