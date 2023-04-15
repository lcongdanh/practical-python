# mortgage.py
#
# Exercise 1.7
principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0
month_num = 0
extra_payment_start_month = 61
extra_payment_end_month = 108
extra_payment = 1000

while principal > 0:
    if payment > principal:
        payment = principal * (1+rate/12)
        principal = 0
        total_paid = total_paid + payment
        month_num+=1

    else:
        principal = principal * (1+rate/12) - payment
        total_paid = total_paid + payment
        month_num+=1

    if month_num >= extra_payment_start_month and month_num <= extra_payment_end_month:
        principal = principal - extra_payment
        total_paid = total_paid + extra_payment

    # print(month_num,round(total_paid,2),round(principal,2))

print(f'Total paid {total_paid:0.2f}')
print(f'Total months {month_num}')