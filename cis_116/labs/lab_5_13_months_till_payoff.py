loan = float(input())
amt = float(input())
interest = float(input())
payments = 0

while loan > 0:
    loan += (loan * interest)
    loan -= amt
    payments += 1

if payments == 1:
    print(f'{payments} payment')
else:
    print(f'{payments} payments')
    