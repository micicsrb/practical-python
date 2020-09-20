# mortgage.py
#
# Exercise 1.7

principal = 5e5
rate = 0.05
payment = 2684.11
total_paid = 0.0
month = 0

extra_payment_start_month = 61
extra_payment_end_month = 108
extra_payment = 1000

while principal > 0:
    month += 1

    if month == extra_payment_start_month:
        payment += extra_payment
    elif month == extra_payment_end_month + 1:
        payment -= extra_payment

    principal = principal * (1 + rate / 12) - payment
    total_paid += payment

    if principal < 0:
        total_paid += principal
        principal = 0

    print(month, round(total_paid, 2), round(principal, 2))

print('Total paid', round(total_paid, 2))
print('Months', month)
