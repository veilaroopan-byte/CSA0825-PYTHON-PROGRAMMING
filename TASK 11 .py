from decimal import Decimal, ROUND_HALF_UP
import json

# Rate card
RATE_CARD = {
    "base_rate": "32.00",
    "fat_step": "0.45",
    "snf_step": "0.30",
    "standard_fat": "3.50",
    "standard_snf": "8.50",
    "bonus_limit": "500",
    "bonus_rate": "0.50"
}

def rate_per_litre(fat, snf):
    """Calculate the milk rate per litre."""
    fat_steps = round((fat - 3.50) / 0.10)
    snf_steps = round((snf - 8.50) / 0.10)

    rate = (
        Decimal(RATE_CARD["base_rate"])
        + Decimal(fat_steps) * Decimal(RATE_CARD["fat_step"])
        + Decimal(snf_steps) * Decimal(RATE_CARD["snf_step"])
    )
    return rate.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)

def payout(litres, fat, snf):
    """Calculate payment for a milk entry."""
    if litres < 0 or not 2.00 <= fat <= 7.00 or snf < 0:
        raise ValueError("Invalid milk entry")
    return (Decimal(str(litres)) * rate_per_litre(fat, snf)).quantize(
        Decimal("0.01"), rounding=ROUND_HALF_UP
    )

def ten_day_total(entries):
    """Calculate ten-day payment with a bonus above 500 litres."""
    total_litres = sum(Decimal(str(entry[0])) for entry in entries)
    total_payment = sum(
        (payout(*entry) for entry in entries), Decimal("0.00")
    )

    if total_litres > Decimal(RATE_CARD["bonus_limit"]):
        total_payment += total_litres * Decimal(RATE_CARD["bonus_rate"])

    return total_payment.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)

# Example: April–June seasonal rate
entries = [
    (10, 3.50, 8.50),
    (8.5, 4.20, 8.70),
    (12, 3.10, 8.30)
]

try:
    for litres, fat, snf in entries:
        print(
            f"Rate: Rs.{rate_per_litre(fat, snf):.2f}, "
            f"Payment: Rs.{payout(litres, fat, snf):.2f}"
        )

    print("Ten-day total: Rs.", ten_day_total(entries))
except ValueError as error:
    print("Error:", error)