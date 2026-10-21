from decimal import Decimal
from time import perf_counter

PAYMENT = "33.40"
COUNTS = [300, 6000, 150000]

for n in COUNTS:
    payments = [PAYMENT] * n

    start = perf_counter()
    float_total = sum(float(x) for x in payments)
    float_time = perf_counter() - start

    start = perf_counter()
    decimal_total = sum(Decimal(x) for x in payments)
    decimal_time = perf_counter() - start

    print(f"\nPayments: {n}")
    print(f"Float total: {float_total:.2f}")
    print(f"Decimal total: {decimal_total:.2f}")
    print(f"Difference: {abs(Decimal(str(float_total)) - decimal_total):.6f}")
    print(f"Float time: {float_time:.6f} seconds")
    print(f"Decimal time: {decimal_time:.6f} seconds")

# Compare rounding methods
payments = [Decimal("33.335")] * 5
rounded_each = sum(x.quantize(Decimal("0.01")) for x in payments)
rounded_total = sum(payments).quantize(Decimal("0.01"))

print("\nRounded each payment:", rounded_each)
print("Rounded final total:", rounded_total)

# Rate table example
rate_card = {
    (3.5, 8.5): 30.00,
    (4.2, 8.7): 33.40
}

print("Stored rate:", rate_card[(4.2, 8.7)])