from decimal import Decimal, ROUND_HALF_UP

BASE_RATE = Decimal("32.00")
FAT_STEP_VALUE = Decimal("0.45")
SNF_STEP_VALUE = Decimal("0.30")
BONUS_LIMIT = Decimal("500")
BONUS_RATE = Decimal("0.50")

def rate_per_litre(fat, snf):
    """Calculate milk rate per litre."""
    fat = Decimal(str(fat))
    snf = Decimal(str(snf))

    fat_steps = round((fat - Decimal("3.50")) / Decimal("0.10"))
    snf_steps = round((snf - Decimal("8.50")) / Decimal("0.10"))

    rate = (BASE_RATE
            + fat_steps * FAT_STEP_VALUE
            + snf_steps * SNF_STEP_VALUE)

    return rate.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)

def payout(litres, fat, snf):
    """Calculate payment for milk supplied."""
    litres = Decimal(str(litres))
    if litres < 0 or not Decimal("2.00") <= Decimal(str(fat)) <= Decimal("7.00") or Decimal(str(snf)) < 0:
        raise ValueError("Invalid milk entry")

    return (litres * rate_per_litre(fat, snf)).quantize(
        Decimal("0.01"), rounding=ROUND_HALF_UP
    )

def bonus(total_litres):
    """Calculate bonus when supply exceeds 500 litres."""
    total_litres = Decimal(str(total_litres))
    if total_litres > BONUS_LIMIT:
        return (total_litres * BONUS_RATE).quantize(
            Decimal("0.01"), rounding=ROUND_HALF_UP
        )
    return Decimal("0.00")

def ten_day_total(entries):
    """Calculate ten-day payment and bonus."""
    total_litres = sum(Decimal(str(e[0])) for e in entries)
    total_payment = sum(
        (payout(litres, fat, snf) for litres, fat, snf in entries),
        Decimal("0.00")
    )
    return total_payment + bonus(total_litres)

# Test entries: litres, fat, SNF
entries = [
    (200, "3.50", "8.50"),
    (180, "4.20", "8.70"),
    (150, "3.10", "8.30")
]

try:
    print("Rate per litre:", rate_per_litre("4.20", "8.70"))
    print("Payment:", payout(10, "4.20", "8.70"))
    print("Bonus:", bonus(501))
    print("Ten-day total:", ten_day_total(entries))
except ValueError as error:
    print("Error:", error)