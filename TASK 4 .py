import math

fat = 4.2
snf = 8.5

BASE_RATE = 30.0
FAT_RATE = 0.40
SNF_RATE = 0.30

fat_steps = round((fat - 3.5) / 0.1)
snf_steps = round((snf - 8.0) / 0.1)

rate = BASE_RATE + fat_steps * FAT_RATE + snf_steps * SNF_RATE
amount = 10 * rate

print("Fat steps:", fat_steps)
print("SNF steps:", snf_steps)
print("Rate per litre:", rate)
print("Amount:", amount)

print("Division:", (4.2 - 3.5) / 0.1)
print("Round:", round(-7.8))
print("Int:", int(-7.8))
print("Floor:", math.floor(-7.8))
print("Valid fat:", 2.0 <= fat <= 7.0)